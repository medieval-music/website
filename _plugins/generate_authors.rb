# _plugins/generate_author_and_editor_pages.rb

module Jekyll
  class GenerateAuthorAndEditorPages < Jekyll::Generator
    safe true
    priority :low

    def generate(site)
	  canonical_names = load_canonical_names(site)

      authors_books = Hash.new { |hash, key| hash[key] = { authored: [], edited: [] } }
      all_authors = Set.new  # A set to collect all unique authors and editors

      # Step 1: Collect all pages with author/editor references, but only scan pages with 'book' layout
      site.pages.each do |page|
        # Only process pages that have the 'book' layout
        if page.data['layout'] == 'book'
          author_names = extract_authors(page, canonical_names)
          editor_names = extract_editors(page, canonical_names)

          # Add authors and editors to the respective books lists
          author_names.each do |author|
            authors_books[author][:authored] << page
            all_authors.add(author)
          end

          editor_names.each do |editor|
            authors_books[editor][:edited] << page
            all_authors.add(editor)
          end
        end
      end

      # Step 2: Update or create author/editor pages with the list of books (authored and edited)
      authors_books.each do |name, books|
        author_slug = Jekyll::Utils.slugify(name)

        # Check if an author/editor page already exists
        author_page = find_author_page(site, author_slug)
        if author_page
          # Existing page: replace the books field with the new list
          replace_books_in_author_page(author_page, books)
        else
          # No author/editor page exists: create a new virtual page
          create_author_page(site, name, books)
        end
      end

      # Step 3: Store the list of authors and editors in the site data
      site.data['authors'] = all_authors.to_a.sort.map do |name|
        author_slug = Jekyll::Utils.slugify(name)
        {
          'name' => name,
          'url' => "/authors/#{author_slug}.html"  # URL to the author's page
        }
      end
    end

    private
	
	# Load the canonical names map from the data file
    def load_canonical_names(site)
      site.data['authors_canonical_names'] || {}
    end

    # Extract authors from the page front matter
    def extract_authors(page, canonical_names)
      authors = []

      # Handle 'author', 'author2'... 'author99'
      (1..99).each do |i|
        author_key = i == 1 ? 'author' : "author#{i}"
        if page.data[author_key]
          authors << normalize_name(page.data[author_key], canonical_names)
        end
      end

      # Handle 'authors' array
      if page.data['authors'].is_a?(Array)
        authors.concat(page.data['authors'].map { |author| normalize_name(author, canonical_names) })
      end

      authors.compact.uniq
    end

    # Extract editors from the page front matter
    def extract_editors(page, canonical_names)
      editors = []

      # Handle 'editor', 'editor2'... 'editor99'
      (1..99).each do |i|
        editor_key = i == 1 ? 'editor' : "editor#{i}"
        if page.data[editor_key]
          editors << normalize_name(page.data[editor_key], canonical_names)
        end
      end

      # Handle 'editors' array
      if page.data['editors'].is_a?(Array)
        editors.concat(page.data['editors'].map { |editor| normalize_name(editor, canonical_names) })
      end

      editors.compact.uniq
    end
	
	# Normalize name based on the canonical names map
    def normalize_name(name, canonical_names)
      canonical_names[name.to_s.downcase] || name # Return the canonical name if it exists, otherwise return the original name
    end

    # Check if an author/editor page exists (physical page check)
    def find_author_page(site, author_slug)
      author_page_path = File.join(site.source, 'authors', "#{author_slug}.md")
      if File.exist?(author_page_path)
        site.pages.find { |p| p.path == "authors/#{author_slug}.md" }
      else
        nil
      end
    end

    # Replace the books fields in the front matter of the author/editor page
    def replace_books_in_author_page(author_page, books)
      # Replace the books fields (authored and edited)
      author_page.data['authored_books'] = books[:authored].map { |page| { 'title' => page.data['title'], 'url' => page.url } }
      author_page.data['edited_books'] = books[:edited].map { |page| { 'title' => page.data['title'], 'url' => page.url } }
    end

    # Create a new virtual author/editor page if it doesn't exist
    def create_author_page(site, name, books)
      author_slug = Jekyll::Utils.slugify(name)
      author_page = Jekyll::Page.new(site, site.source, 'authors', "#{author_slug}.md")
      author_page.data['layout'] = 'author'
      author_page.data['title'] = "Books by #{name}"
      author_page.data['author_name'] = name

      # Populate the books data (authored and edited)
      author_page.data['authored_books'] = books[:authored].map { |page| { 'title' => page.data['title'], 'url' => page.url } }
      author_page.data['edited_books'] = books[:edited].map { |page| { 'title' => page.data['title'], 'url' => page.url } }

      site.pages << author_page
    end
  end
end

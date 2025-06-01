require 'active_support'
require 'active_support/inflector'

# Jekyll filter for sorting titles while ignoring specific starting words
# Uses ignore_words site data (found in _data/ignore_words.yml) for the list of starting words to ignore while sorting
# Populates sort_title front matter with the title used for sorting (ie. lowercase title with all "ignore words" removed)
# Populates group_letter front matter with the letter coresponding to the group that should contain the title
# Sorts based off of the title front matter
# Uses ActiveSupport Transliterate to handle special unicode characters in order to sort using the ASCII equivalent
module Jekyll
  module SortByTitleIgnoreWords
    def sort_by_title_ignore_words(input, site)
      # Load the ignore words from the site's data directory
      ignore_words = site.data['ignore_words'] || []

      input.sort_by do |item|
        # Extract the title to sort by
        title = item.data['title'].to_s.downcase.strip

        # Remove punctuation from the title (ignores leading punctuation and spaces)
        title = title.gsub(/^\p{P}+/,'') # Remove punctuation from the start
        title = title.gsub(/[[:punct:]]+$/, '') # Remove punctuation from the end

        # Remove the leading word if it's in the ignore_words list
        ignore_words.each do |word|
          # Check if the title starts with the ignored word
          if title.start_with?("#{word} ")
            title = title.sub(/^#{word} /, '')
            break
          end
        end
		
		# Transliterate for sorting/grouping (Ü → U, etc.)
        sort_title = ActiveSupport::Inflector.transliterate(title).strip

        # Determine group letter
        group_letter = sort_title[0]&.upcase || '#'
        group_letter = '#' unless group_letter =~ /[A-Z]/

        # Store cleaned data in item for use in Liquid
        item.data['sort_title'] = sort_title
        item.data['group_letter'] = group_letter

        sort_title
      end
    end
  end
end

# Register the filter with Liquid
Liquid::Template.register_filter(Jekyll::SortByTitleIgnoreWords)

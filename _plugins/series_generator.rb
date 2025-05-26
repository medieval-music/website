module Jekyll
  class SeriesPage < Page
	def initialize(site, series_key, series_title, series_slug)
	  @site = site
	  @base = site.source
	  @dir = 'series'

	  @basename = series_slug
	  @ext = '.html'
	  @name = "#{series_slug}.html"

	  @data = {
	    'title' => series_title,
		'series' => series_key,
		'layout' => 'series'
	  }

	  data.default_proc = proc do |_, key|
        site.frontmatter_defaults.find(relative_path, :authors, key)
      end
	end

	def url_placeholders
      {
        :path       => @dir,
        :category   => @dir,
        :basename   => basename,
        :output_ext => output_ext,
      }
    end
  end

  class SeriesPageGenerator < Generator
    safe true
    priority :low  # Run after other plugins

    def generate(site)
      series_map = site.data["series_names"] || {}
      seen_series = Set.new

      site.pages.each do |page|
        next unless page.data["layout"] == "book"

        # Use series from front matter, or infer from path
        series_key = page.data["series"]

        if series_key.nil? && page.path.start_with?("books/")
          path_parts = page.path.split("/")
          if path_parts.size > 1
            series_key = path_parts[1]
            page.data["series"] = series_key  # Auto-tag the page
          end
        end

        seen_series << series_key if series_key
      end

      # Generate index page for each detected series
      seen_series.each do |series_key|
        series_title = series_map[series_key] || series_key.capitalize
		series_slug = Jekyll::Utils.slugify(series_key)
        site.pages << SeriesPage.new(
          site,
          series_key,
          series_title,
          series_slug
        )
      end
	  
	  site.data["series"] = seen_series.to_a.sort
    end
  end
end

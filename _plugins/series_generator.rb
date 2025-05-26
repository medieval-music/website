module Jekyll
  class SeriesPage < Page
    def initialize(site, base, dir, series_key, series_title)
      @site = site
      @base = base
      @dir = dir
      @name = "index.html"

      self.process(@name)
      self.read_yaml(File.join(base, "_layouts"), "series.html")

      self.data["title"] = "#{series_title} Series"
      self.data["series"] = series_key
      self.data["permalink"] = "/series/#{series_key}/"
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
        site.pages << SeriesPage.new(
          site,
          site.source,
          File.join("series", series_key),
          series_key,
          series_title
        )
      end
	  
	  site.data["series"] = seen_series.to_a.sort
    end
  end
end

module Jekyll
  module ChicagoCitationFilter
    def chicago_citation(page, site)
      authors = page['author_names'] || []
      editors = page['editor_names'] || []
      title = page['title']
      volume = page['volume']
      place = page['place'] || "Ottawa"
      publisher = page['publisher'] || "IMM"

      raw_year = (page['year'] || '').to_s.strip

      series_key = page['series']
      series_name = site['data']['series_names'][series_key] if series_key

      # Year handling with n.d and optional <time>
      if raw_year.empty?
        year_display = "n.d"
        year_iso = nil
      else
        match = raw_year.match(/\d{4}/)
        year_iso = match ? match[0] : nil
        year_display = raw_year
      end

      citation = ""

      # 1. Author or editor names in bibliographic format
      if !authors.empty?
        citation += "#{format_name_list_biblio(authors)}. "
      elsif !editors.empty?
        citation += "#{format_name_list_biblio(editors)}, #{editors.length == 1 ? 'ed.' : 'eds.'}. "
      end

      # 2. Title (italicized)
      citation += "<em>#{title}</em>. "

      # 3. Edited by (if both authors and editors present)
      if !authors.empty? && !editors.empty?
        citation += "Edited by #{format_name_list(editors)}. "
      end

      # 4. Series + Volume
      if series_name && volume
        citation += "#{series_name} #{volume}. "
      elsif series_name
        citation += "#{series_name}. "
      end

      # 5. Place, publisher, year (with optional <time>)
      if year_iso
        citation += "#{place}: #{publisher}, <time datetime=\"#{year_iso}\">#{year_display}</time>."
      else
        citation += "#{place}: #{publisher}, #{year_display}."
      end

      citation.strip
    end

    private

    # Format names for bibliography: first name inverted, others normal
    def format_name_list_biblio(names)
      names = names.map(&:strip)
      return names[0] if names.length == 1

      if names.length == 2
        "#{invert_name(names[0])} and #{names[1]}"
      else
        first = invert_name(names[0])
        middle = names[1..-2].join(', ')
        last = names[-1]
        "#{first}, #{middle}, and #{last}"
      end
    end

    # Format names in natural order (for "Edited by ...")
    def format_name_list(names)
      names = names.map(&:strip)
      return names[0] if names.length == 1
      return names.join(' and ') if names.length == 2
      [names[0..-2].join(', '), names[-1]].join(', and ')
    end

    # Invert a name like "Last, First" to "Last, First" (keeps as is)
    # but this method is kept for clarity and possible future tweaks
    def invert_name(name)
      parts = name.split(',', 2).map(&:strip)
      return name unless parts.length == 2
      "#{parts[0]}, #{parts[1]}"
    end
  end
end

Liquid::Template.register_filter(Jekyll::ChicagoCitationFilter)

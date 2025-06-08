# Jekyll filter for sorting books by volume
# Sorts based off of the volume front matter and volume_part front matter if it exists
module Jekyll
  module SortByVolume

    ROMAN_MAP = {
      "M"=>1000, "CM"=>900, "D"=>500, "CD"=>400,
      "C"=>100, "XC"=>90, "L"=>50, "XL"=>40,
      "X"=>10, "IX"=>9, "V"=>5, "IV"=>4, "I"=>1
    }

    def roman_to_int(roman)
      return 0 unless roman
      s = roman.upcase
      i = 0
      num = 0
      while i < s.length
        if i + 1 < s.length && ROMAN_MAP[s[i..i+1]]
          num += ROMAN_MAP[s[i..i+1]]
          i += 2
        else
          num += ROMAN_MAP[s[i]]
          i += 1
        end
      end
      num
    end

    def normalize_part(part)
      return ['000', ''] unless part
	  
	  part = part.to_s

      match = part.match(/^(\d+)([a-zA-Z]*)$/)
      num = match ? match[1].rjust(3, '0') : '000'
      suffix = match ? match[2].downcase : ''
      [num, suffix]
    end

    def sort_by_volume(docs)
      docs.sort_by do |doc|
        vol = roman_to_int(doc['volume'])
        part_num, part_suffix = normalize_part(doc['volume_part'])
        [vol, part_num, part_suffix]
      end
    end

  end
end

Liquid::Template.register_filter(Jekyll::SortByVolume)

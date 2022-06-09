# Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.
# For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".

def finds(s, k)
  arr = s.scan /\w/
  max = 0
  longest_word = ''
  total_length = arr.length
  last_idx = total_length - 1
  arr.each_with_index do |l, i|
    p "first letter: #{l}"
    start_slice = i
    (i+1..last_idx).each do |j| 
      p "max: #{max}"
      sub_array = arr.slice(i,j)
      next if j + max  > total_length
      next if sub_array.length <= max
      p "sub_array: #{sub_array}"
      if sub_array.uniq.length <= k
        if max < sub_array.length
          longest_word = sub_array.join("")
          max = sub_array.length
        end
      else
        break
      end
    end
  end
  return longest_word
end

finds("abcba", 2) == "bcb"
finds("abcbavqerbcccbb", 2) == "bcccbb"

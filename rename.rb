name_list = File.open("filenameslist.txt").read
save_list = File.open "rubymovie.txt", "w"

name_list.each_line do |line|
  text = line.strip
  text =~ /([^\\]+)\.(avi|mkv|mpeg|mpg|mov|mp4|iso)$/
  text = $1 if $1
  text.gsub!(".", " ")
  text =~ /(.*?)(dvdrip|xvid| cd[0-9]|dvdscr|brrip|divx|[\{\(\[]?[0-9]{4}).*/
  text = $1 if $1
  text =~ /(.*?)\(.*\)(.*)/
  text = $1 if $1

  puts text
  save_list.write text + "\n"
end
save_list.close


def extract_movie_name(name)
    
end

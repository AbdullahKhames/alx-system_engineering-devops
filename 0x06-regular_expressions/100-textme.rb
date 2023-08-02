#!/usr/bin/env ruby
#script to get data from logs

if ARGV.empty?
	puts "Usage: ruby 100-textme.rb 'log_entry'"
	exit(1)
  end
  
  log_entry = ARGV[0]
  
  regex = /\[from:(.*?)\] \[to:(.*?)\] \[flags:(.*?)\]/
  
  match_data = log_entry.match(regex)
  
  if match_data
	sender = match_data[1]
	receiver = match_data[2]
	flags = match_data[3]
  
	puts "#{sender},#{receiver},#{flags}"
  else
	puts "No match found in the log entry."
  end

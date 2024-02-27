#!/usr/bin/env ruby
puts ARGV[0].to_s.scan(/^(.{5,8})$/).join('')

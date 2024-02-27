#!/usr/bin/env ruby
puts ARGV[0].to_s.scan(/^(.{3,4})$/).join('')

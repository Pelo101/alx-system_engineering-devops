#!/usr/bin/env ruby
puts ARGV[0].to_s.scan(/^(.{4,6})$/).join('')

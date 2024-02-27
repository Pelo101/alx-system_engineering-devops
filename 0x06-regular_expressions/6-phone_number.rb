#!/usr/bin/env ruby
puts ARGV[0].to_s.scan(/^[0-9]{10}$/).join('')

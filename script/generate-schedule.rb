#!/usr/bin/env ruby
 
require 'time'
 
FIRSTSUNDAY=13
 
start = Time.local(2013, 1, FIRSTSUNDAY, 9, 00)
 
wsecs=604800
 
users = ["Curt", "Jason"]
u = 0
tick = 1
d = start
while d.year < 2014
  sched = users[u]
  puts "#{d.strftime("%b").upcase} #{d.strftime("%d")}: #{sched}"
  d = d + wsecs
 
  case tick
  when 1
    u = u
    tick = tick + 1
  when 2
    if u == (users.length - 1)
      u = 0
    else
      u = u + 1
    end
    tick = 1
  end
end

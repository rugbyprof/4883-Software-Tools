select id,count(id) from (SELECT id,name,season,count(club) as count,club FROM `players` group by club,id) as counts group by id ORDER BY `count(id)` DESC

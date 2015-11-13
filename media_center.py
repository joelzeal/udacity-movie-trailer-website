import media
import fresh_tomatoes

# create instances of movie
the_grey = media.Movie(
  "The Grey",
  "Following a grueling five-week shift at an Alaskan oil refinery, \
  workers led by sharpshooter John Ottway (Liam Neeson) are flying home \
  for a much-needed vacation. A brutal storm causes their plane to \
  crash in the frozen wilderness, and only eight men (Frank Grillo, \
  Dermot Mulroney), including Ottway, survive. As they trek southward \
  toward civilization and safety, Ottway and his companions \
  must battle mortal injuries, the icy elements, and a pack of \
  hungry wolves.",
  "http://gdj.gdj.netdna-cdn.com/wp-content/uploads/2011/12/grey-movie-poster.jpg",  # noqa
  "https://www.youtube.com/watch?v=Hfb0-U0ydj8",
  "Liam Neeson",
  "2012")


casino_royale = media.Movie(
  "Casino Royale",
  "After receiving a license to kill, British Secret Service agent \
  James Bond (Daniel Craig) heads to Madagascar, where he uncovers \
  a link to Le Chiffre (Mads Mikkelsen), a man who finances terrorist \
  organizations. Learning that Le Chiffre plans to raise money in a \
  high-stakes poker game, MI6 sends Bond to play against him, \
  gambling that their newest operative will topple the man's organization",
  "http://images4.fanpop.com/image/photos/22800000/-movie-posters-22851131-1000-1489.jpg",   # noqa
  "https://www.youtube.com/watch?v=36mnx8dBbGE",
  "James Bond",
  "2006")

jonny_english = media.Movie(
  "Jonny English Reborn",
  "After a disastrous mission in Mozambique, British agent Johnny English \
  (Rowan Atkinson) has retreated to a Tibetan monastery to try to forget\
  his shame. But when he receives an urgent call from MI-7 to lead a \
  mission that only he can handle, English is back in action. Using \
  his questionable combat ",
  "http://images5.fanpop.com/image/photos/26200000/Johhny-English-movie-posters-26233319-1012-1500.jpg",  # noqa
  "www.youtube.com/watch?v=JSg2tgnvtgY",
  "Rowan Atkinson",
  "2011")

the_expendables = media.Movie(
  "The Expendables 2",
  "This is the story of a boy and his toys",
  "http://t3.gstatic.com/images?q=tbn:ANd9GcQ9qF-tGkwN1qzXOX0SHFHGO3WUmIhxN8nqmzjpmpuntltW9Pn6",  # noqa
  "www.youtube.com/watch?v=7rkdTcQLwZ4",
  "Sylvester Stallone",
  "2012")

game_of_Shadows = media.Movie(
  "A Game of Shadows",
  "When Austria's crown prince is found dead, evidence seems to point \
  to suicide. However, detective Sherlock Holmes (Robert Downey Jr.) \
  deduces that the prince was murdered and that the crime is but a \
  piece of a puzzle designed by an evil genius named Moriarty (Jared Harris).",
  "http://images5.fanpop.com/image/photos/26500000/Robert-Downey-Jr-SH2-Movie-Posters-robert-downey-jr-26552470-453-660.jpg",  # noqa
  "www.youtube.com/watch?v=td2Zjdjqhhs",
  "Robert Downey Jr.",
  "2011")

thor = media.Movie(
  "Thor",
  "As the son of Odin (Anthony Hopkins), king of the Norse gods, \
  Thor (Chris Hemsworth) will soon inherit the throne of Asgard \
  from his aging father. However, on the day that he is to be crowned, \
  Thor reacts with brutality when the gods' enemies, the Frost Giants, \
  enter the palace in violation of their treaty. As punishment, \
  Odin banishes Thor to Earth. While Loki (Tom Hiddleston), Thor's \
  brother, plots mischief in Asgard, Thor, now stripped of his powers, \
  faces his greatest threat.",
  "http://img2.wikia.nocookie.net/__cb20110601084658/marvelmovies/images/9/9a/Thor_Movie_Poster-Thor.jpg",  # noqa
  "www.youtube.com/watch?v=JOddp-nlNvQ",
  "Anthony Hopkins",
  "2011")

# create an array of movies
movies = [the_grey, casino_royale, jonny_english, the_expendables,
          game_of_Shadows, thor]

# pass movies array to open_movies_page for movies page to be generated.
fresh_tomatoes.open_movies_page(movies)

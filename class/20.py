class Movie:
  def __init__(self, name, dir):
    self.__name = name
    self.__dir = dir
    self.__reviews = {}

  def add_review(self, name, review):
    print("Thanks for reviewing!!")
    self.__reviews[name] = review

  def get_review(self, name):
    if name not in self.__reviews:
      return f"No review done by {name}"
    else:
      return self.__reviews[name]


movie1 = Movie("Interstellar", "Christopher Nolan")

movie1.add_review("Eren", "One of the greatest sci-fi movies ever!")
movie1.add_review("Armin", "Amazing visuals and mind-blowing storyline.")
movie1.add_review("Mikasa", "A masterpiece with emotional depth.")
movie1.add_review("Levi", "Great cinematography and soundtrack.")

print("\n--- Movie Reviews ---")
print("Eren:", movie1.get_review("Eren"))
print("Armin:", movie1.get_review("Armin"))
print("Mikasa:", movie1.get_review("Mikasa"))
print("Levi:", movie1.get_review("Levi"))

print("Jean:", movie1.get_review("Jean"))

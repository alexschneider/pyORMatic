import databaseobject
import table
import pickledatabase

db = pickledatabase.PickleDatabase("ch2", "db")
tab = table.Table(db, "ratings")
def add_ratings():
    users = {"Angelica": {"Blues Traveler": 3.5, "Broken Bells": 2.0, "Norah Jones": 4.5, "Phoenix": 5.0, "Slightly Stoopid": 1.5, "The Strokes": 2.5, "Vampire Weekend": 2.0},
         "Bill":{"Blues Traveler": 2.0, "Broken Bells": 3.5, "Deadmau5": 4.0, "Phoenix": 2.0, "Slightly Stoopid": 3.5, "Vampire Weekend": 3.0},
         "Chan": {"Blues Traveler": 5.0, "Broken Bells": 1.0, "Deadmau5": 1.0, "Norah Jones": 3.0, "Phoenix": 5, "Slightly Stoopid": 1.0},
         "Dan": {"Blues Traveler": 3.0, "Broken Bells": 4.0, "Deadmau5": 4.5, "Phoenix": 3.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 2.0},
         "Hailey": {"Broken Bells": 4.0, "Deadmau5": 1.0, "Norah Jones": 4.0, "The Strokes": 4.0, "Vampire Weekend": 1.0},
         "Jordyn":  {"Broken Bells": 4.5, "Deadmau5": 4.0, "Norah Jones": 5.0, "Phoenix": 5.0, "Slightly Stoopid": 4.5, "The Strokes": 4.0, "Vampire Weekend": 4.0},
         "Sam": {"Blues Traveler": 5.0, "Broken Bells": 2.0, "Norah Jones": 3.0, "Phoenix": 5.0, "Slightly Stoopid": 4.0, "The Strokes": 5.0},
         "Veronica": {"Blues Traveler": 3.0, "Norah Jones": 5.0, "Phoenix": 4.0, "Slightly Stoopid": 2.5, "The Strokes": 3.0}
    }
    user_objs = list()
    for user, items in users.items():
        user_objs.append(databaseobject.DatabaseObject(user=user, ratings=items))
    tab.put(user_objs)
def manhattan(rating1, rating2):
    """Computes the Manhattan distance. Both rating1 and rating2 are dictionaries
       of the form {'The Strokes': 3.0, 'Slightly Stoopid': 2.5}"""
    distance = 0
    commonRatings = False 
    for key in rating1:
        if key in rating2:
            distance += abs(rating1[key] - rating2[key])
            commonRatings = True
    if commonRatings:
        return distance
    else:
        return -1 #Indicates no ratings in common


def computeNearestNeighbor(username, table):
    """creates a sorted list of users based on their distance to username"""
    distances = []
    to_compute = next(table.get_fields(user=username))
    for user in table:
        if user["user"] != username:
            distance = manhattan(user["ratings"], to_compute["ratings"])
            distances.append((distance, user["user"]))
    # sort based on distance -- closest first
    distances.sort(key=lambda x: x[0])
    return distances

def recommend(username, table):
    """Give list of recommendations"""
    # first find nearest neighbor
    nearest = computeNearestNeighbor(username, table)[0][1]

    recommendations = []
    # now find bands neighbor rated that user didn't
    neighborRatings = table.get_one(user=nearest)
    userRatings = table.get_one(user=username)
    for artist in neighborRatings["ratings"]:
        if not artist in userRatings["ratings"]:
            recommendations.append((artist, neighborRatings["ratings"][artist]))
    return sorted(recommendations, key=lambda artistTuple: artistTuple[1], reverse=True)

def pearson(recommendation1, recommendation2):
    rec_set = recommendation1.keys() & recommendation2.keys()
    first_num = 0
    rec1_sum = 0
    rec2_sum = 0
    rec1_sqr = 0
    rec2_sqr = 0
    for key in rec_set:
        first_num += recommendation1[key] * recommendation2[key]
        rec1_sum += recommendation1[key]
        rec2_sum += recommendation2[key]
        rec1_sqr += recommendation1[key]**2
        rec2_sqr += recommendation2[key]**2
    second_num = (rec1_sum + rec2_sum) / len(rec_set)
    num = first_num - second_num
    find_den = lambda x, y, z: (x - y**2/len(z))**(1/2)
    first_den = find_den(rec1_sqr, rec1_sum, rec_set)
    second_den = find_den(rec2_sqr, rec2_sum, rec_set)
    return (first_num - second_num)/(first_den * second_den)

# uncomment the next line to initialize the database
#add_ratings()



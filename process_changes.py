## all imports at top
import math

## open the file - and read all of the lines.
changes_file = 'changes_python.txt'

## use strip to strip out spaces and trim the line.
data = [line.strip() for line in open(changes_file, 'r')]

## print the number of lines read
print "Number of lines read:\t\t", len(data)

## separator is 72 hyphens
sep = 72*'-'

## create the commit class to hold each of the elements
## check there are 422 entries 
class Commit:
    'class for commits'
   
   ## instance variables
    def __init__(self, revision = None, author = None, date = None, comment_line_count = None, changes = None, comment = None):
        self.revision = revision
        self.author = author
        self.date = date
        self.comment_line_count = comment_line_count
        self.changes = changes
        self.comment = comment
    
    ## define get_commit_comment
    def get_commit_comment(self):
        return 'svn merge -r' + str(self.revision-1) + ':' + str(self.revision) + ' by ' \
                + self.author + ' with the comment ' + ','.join(self.comment) \
                + ' and the changes ' + ','.join(self.changes)

## create empty arrays
commits = []
changes = []
authors = []
dates = []
comment_line_counts = []

current_commit = None

## set index
index = 0

## create empty author
author = {}
while True:
    try:
        ## parse each of the commits and put them into a list of commits
        current_commit = Commit()
        details = data[index + 1].split('|')
        ## use position in details array to assign values to variables
        current_commit.revision = int(details[0].strip().strip('r'))
        current_commit.author = details[1].strip()
        current_commit.date = details[2].strip()
        current_commit.comment_line_count = int(details[3].strip().split(' ')[0])
        current_commit.changes = data[index+2:data.index('',index+1)]
        #print(current_commit.changes)
        changed_paths = data[index + 1]
        index = data.index(sep, index + 1)
        current_commit.comment = data[index-current_commit.comment_line_count:index]
        ## populate arrays
        commits.append(current_commit)
        changes.append(changed_paths)
        authors.append(current_commit.author)
        dates.append(current_commit.date)
        comment_line_counts.append(current_commit.comment_line_count)
    except IndexError:
        break

## define most common function
def most_common(array):
    return max( set(array), key = array.count )

## calculate mean
mean_comment_line_counts = ( sum(comment_line_counts) / len(comment_line_counts) )
## calculate standard deviation
for i in range(0, len(comment_line_counts)-1):
    stdev_sqrt_sum_squared = math.sqrt(sum(comment_line_counts)**2 )
stdev_comment_line_counts = float ( stdev_sqrt_sum_squared / len(comment_line_counts) )
    
print "Total number of commits:\t", len(commits)
#print "Number of changed paths:\t", len(changes)
print   "Number of unique authors:\t", len(set(authors))

## call most common function for authors
most_common(authors)
print   "Most common author:\t\t", most_common(authors)

## call most common function for dates
most_common(dates)
print   "Most common date:\t\t", most_common(dates)

print   "Max comment line counts:\t", max(comment_line_counts)
print   "Min comment line counts:\t", min(comment_line_counts)
print   "Mean comment line counts:\t", round(mean_comment_line_counts, 2)
print   "Standard deviation cl counts:\t", round(stdev_comment_line_counts, 2)

#commits.reverse()

#for index, commit in enumerate(commits):
    #print(commit.get_commit_comment())
    
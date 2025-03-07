'''
Obeserver Design pattern:
It is a behavioral design pattern where an object (called the subject) maintains a list of
dependents (called observers) that need to be notified of any state changes. It allows a one-to-many
dependency between objects so that when one object changes its state, all its dependents (observers) are
notified automatically.

Use Cases:
    Implementing event-driven systems (e.g., GUI listeners).
    Real-time notifications (e.g., stock price alerts, social media updates).
    Model-View-Controller (MVC) architecture.

Advantages
    ✅ Loose coupling between subject and observers.
    ✅ Easy to extend (add/remove observers dynamically).
    ✅ Improves modularity and maintainability.
'''
from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

class User(Observer):  # Observer class
    '''
    User class will act as observer to subject
    '''
    def __init__(self, name):
        self.name = name

    def update(self, article, blog_writer: "BlogWriter"): # using double quotes in type hint for class defined later
        print(f'For {self.name}, new article {article} by {blog_writer.name} is added')


class BlogWriter:
    '''
    This acts as a subject here(Article to be specific).
    BlogWriter class is useful to blog writer to add new article
    and manage subscribers as well
    '''
    def __init__(self, name):
        self.name = name
        self.__subscribers = [] # Subscribed Users will be added in this list
        self.__articles = [] # Article is the subject

    def add_article(self, article):
        '''
        Add new article and notify subscribers
        '''
        self.__articles.append(article)
        self.notify_subscribers(article)

    def get_articles(self):
        '''
        Get articles written by {self}
        '''
        return self.__articles

    def subscribe(self, subscriber: User):
        '''
        Add new subscriber to notify on adding article
        '''
        self.__subscribers.append(subscriber)

    def unsubscribe(self, subscriber: User):
        '''
        User can unsubscribe from further notifications
        '''
        return self.__subscribers.remove(subscriber)

    def subscribers(self):
        '''
        Get subsribers
        '''
        return self.__subscribers

    def notify_subscribers(self, article):
        '''
        Notifying all the subsribers about new addition of an article
        i.e. Broadcast to all subscribers
        '''
        for sub in self.__subscribers:
            sub.update(article, self)


if __name__ == '__main__':
    blog_writer = BlogWriter('Hardik\'s blog')
    shailaja = User('Shailaja')
    aarav = User('Aarav')
    blog_writer.subscribe(shailaja)
    blog_writer.subscribe(aarav)
    blog_writer.add_article('Article 1')
    blog_writer.unsubscribe(aarav)
    blog_writer.add_article('Article 2')
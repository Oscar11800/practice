from test_runner import assert_equal, run_tests
'''
You have a browser of one tab where you start on the homepage and you can visit another url
get back in the history number of steps or move forward in the history number of steps.

Implement the BrowserHistory class:

BrowserHistory(string homepage) Initializes the object with the homepage of the browser.
void visit(string url) Visits url from the current page. It clears up all the forward history.
string back(int steps) Move steps back in history. 
If you can only return x steps in the history and steps > x, you will return only x steps. 
Return the current url after moving back in history at most steps.
string forward(int steps) Move steps forward in history. 
If you can only forward x steps in the history and steps > x, you will forward only x steps. 
Return the current url after forwarding in history at most steps.
'''

class BrowserNode():

    def __init__(self, url=None, next=None, prev=None):
        self.url = url
        self.next = next
        self.prev = prev
        
class BrowserHistory():

    def __init__(self, homepage):
        """
        :type homepage: str
        """
        self.homepage = BrowserNode(homepage, None, None)
        

    def visit(self, url):
        """
        :type url: str
        :rtype: None
        """
        new_page = BrowserNode(url, None, self.homepage)
        self.homepage.next = new_page
        self.homepage = new_page
        

    def back(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        count = 0
        while self.homepage.prev and count < steps:
            self.homepage = self.homepage.prev
            count += 1
        return self.homepage.url
        

    def forward(self, steps):
        """
        :type steps: int
        :rtype: str
        """
        count = 0
        while self.homepage.next and count < steps:
            self.homepage = self.homepage.next
            count += 1
        return self.homepage.url



# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)

# ========== TESTS ==========
def test1():
    """
    Example case from problem description
    """
    browserHistory = BrowserHistory("leetcode.com")
    
    # Initial state
    assert_equal(browserHistory.back(0), "leetcode.com")  # Should return current page
    
    # Visit sequence
    browserHistory.visit("google.com")       # leetcode.com -> google.com
    browserHistory.visit("facebook.com")     # google.com -> facebook.com
    browserHistory.visit("youtube.com")      # facebook.com -> youtube.com
    
    # Back operations
    result1 = browserHistory.back(1)        # youtube.com -> facebook.com
    assert_equal(result1, "facebook.com")
    
    result2 = browserHistory.back(1)        # facebook.com -> google.com
    assert_equal(result2, "google.com")
    
    # Forward operation
    result3 = browserHistory.forward(1)     # google.com -> facebook.com
    assert_equal(result3, "facebook.com")
    
    # Visit clears forward history
    browserHistory.visit("linkedin.com")     # facebook.com -> linkedin.com (clears forward)
    
    # Forward (can't move forward)
    result4 = browserHistory.forward(2)     # Still at linkedin.com
    assert_equal(result4, "linkedin.com")
    
    # Back operations
    result5 = browserHistory.back(2)         # linkedin.com -> facebook.com -> google.com
    assert_equal(result5, "google.com")
    
    result6 = browserHistory.back(7)        # Can only go back 1 step: google.com -> leetcode.com
    assert_equal(result6, "leetcode.com")


def test2():
    """Test basic visit and back"""
    browserHistory = BrowserHistory("homepage.com")
    
    browserHistory.visit("page1.com")
    browserHistory.visit("page2.com")
    
    assert_equal(browserHistory.back(1), "page1.com")
    assert_equal(browserHistory.back(1), "homepage.com")
    assert_equal(browserHistory.back(1), "homepage.com")  # Can't go back further


def test3():
    """Test forward after back"""
    browserHistory = BrowserHistory("start.com")
    
    browserHistory.visit("a.com")
    browserHistory.visit("b.com")
    browserHistory.visit("c.com")
    
    assert_equal(browserHistory.back(2), "a.com")      # c -> b -> a
    assert_equal(browserHistory.forward(1), "b.com")   # a -> b
    assert_equal(browserHistory.forward(1), "c.com")   # b -> c
    assert_equal(browserHistory.forward(1), "c.com")   # Can't go forward further


def test4():
    """Test visit clears forward history"""
    browserHistory = BrowserHistory("home.com")
    
    browserHistory.visit("a.com")
    browserHistory.visit("b.com")
    browserHistory.back(1)                  # b -> a
    browserHistory.visit("c.com")          # a -> c (should clear forward to b)
    
    assert_equal(browserHistory.forward(1), "c.com")  # Can't go forward (b was cleared)
    assert_equal(browserHistory.back(1), "a.com")


def test5():
    """Test edge cases"""
    browserHistory = BrowserHistory("home.com")
    
    # Back with 0 steps
    assert_equal(browserHistory.back(0), "home.com")
    
    # Forward with 0 steps
    assert_equal(browserHistory.forward(0), "home.com")
    
    # Back more than available
    browserHistory.visit("page.com")
    assert_equal(browserHistory.back(10), "home.com")  # Can only go back 1
    
    # Forward more than available
    browserHistory.back(1)
    assert_equal(browserHistory.forward(10), "page.com")  # Can only go forward 1


if __name__ == "__main__":
    run_tests()
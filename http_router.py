""" HTTPRouter using a Trie """


# Starting at the root, navigate the Trie to find a match for this path
# Return the handler for a match, or None for no match


# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:

    def __init__(self) -> None:
        super().__init__()
        self.children = {}
        self.handler = None

    # Initialize the node with children as before, plus a handler
    def insert(self, path_part):
        if path_part not in self.children:
            self.children[path_part] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, root_handler, not_found_handler):
        self.root = RouteTrieNode()
        self.root.insert('')
        self.root.children[''].handler = root_handler
        self.root.handler = root_handler
        self.not_found_handler = not_found_handler

    # Initialize the trie with an root node and a handler, this is the root path or home page node
    def insert(self, path_parts_list: list[str], handler: str):
        if path_parts_list is None:
            raise ValueError('path_parts_list should not be None')
        if path_parts_list[0] != '':
            raise ValueError('path should start at root')
        current = self.root
        for p in path_parts_list:
            current.insert(p)
            current = current.children[p]
        current.handler = handler

    def find(self, path_parts_list):
        if path_parts_list[-1] == '' and len(path_parts_list) > 1:
            path_parts_list = path_parts_list[:-1]
        current = self.root
        for p in path_parts_list:
            if p not in current.children:
                return self.not_found_handler
            current = current.children[p]
        if current.handler is None:
            return self.not_found_handler
        return current.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self, root_handler : str, not_found_handler : str):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router_trie = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, path: str, handler : str):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path = path.rstrip()
        self.router_trie.insert(self.split_path(path), handler)

    def lookup(self, path : str):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path = path.rstrip()
        return self.router_trie.find(self.split_path(path))

    def split_path(self, path: str):
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        path_parts_list = path.split(sep='/')
        return path_parts_list


def split_path_test():
    router = Router("root handler", "not found handler")
    router.split_path("/home/about/me")
    router.split_path("/")


def my_test():
    # Here are some test cases and expected outputs you can use to test your implementation

    # create the router and add a route
    router = Router("root handler", "not found handler")  # remove the 'not found handler' if you did not implement this
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/"))  # should print 'root handler'
    print(router.lookup("/home"))  # should print 'not found handler' or None if you did not implement one
    print(router.lookup("/home/about"))  # should print 'about handler'
    print(router.lookup("/home/about/"))  # should print 'about handler' or None if you did not handle trailing slashes
    print(router.lookup("/home/about/me"))  # should print 'not found handler' or None if you did not implement one


if __name__ == '__main__':
    # split_path_test()
    my_test()

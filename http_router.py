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
    def __init__(self, root_handler: str, not_found_handler: str):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.router_trie = RouteTrie(root_handler, not_found_handler)

    def add_handler(self, path: str, handler: str):
        # Add a handler for a path
        if path is None:
            raise ValueError('path should not be None')
        if path.rstrip().lstrip() == '':
            raise ValueError('path should not be empty')
        if path[0] != '/':
            raise ValueError('path should start at root')
        if handler is None:
            raise ValueError('handler should not be None')
        if handler == '':
            raise ValueError('handler should not be an empty string')

        path = path.rstrip()
        self.router_trie.insert(self.split_path(path), handler)

    def lookup(self, path: str):
        if path is None:
            raise ValueError('path should not be None')
        if path.rstrip().lstrip() == '':
            raise ValueError('path should not be empty')
        if path[0] != '/':
            raise ValueError('path should start at root')
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


def test1():
    print('\n================================ test1() ================================')
    router = Router("root handler", "not found handler")
    router.add_handler("/home/about", "about handler")  # add a route
    try:
        print(router.lookup(None))
    except Exception as e:
        print(e)  # path should not be None

    try:
        print(router.lookup(''))
    except Exception as e:
        print(e)  # path should not be empty

    try:
        print(router.lookup('somepath'))
    except Exception as e:
        print(e)  # path should start at root


def test2():
    print('\n================================ test2() ================================')
    router = Router("root handler", "not found handler")

    try:
        router.add_handler(None, "about handler")  # add a route
    except Exception as e:
        print(e)  # path should not be None

    try:
        router.add_handler('', "about handler")  # add a route
    except Exception as e:
        print(e)  # path should not be empty

    try:
        router.add_handler('somepath', "about handler")  # add a route
    except Exception as e:
        print(e)  # path should start at root


def test3():
    print('\n================================ test3() ================================')
    router = Router("root handler", "not found handler")
    try:
        router.add_handler('/home/about', None)
    except Exception as e:
        print(e)  # handler should not be None

    try:
        router.add_handler('/home/about', '')
    except Exception as e:
        print(e)  # handler should not be an empty string


def provided_test():
    print('\n================================ provided_test() ================================')
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
    test1()
    test2()
    test3()
    provided_test()

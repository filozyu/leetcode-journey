def simplifyPath(path):
    """
    Convert path (absolute) to a canonical one (never end with "/" except at root)
    Time: O(n)
    Space: O(n)
    """
    stack = []
    for loc in path.split("/"):
        if loc:
            if loc == "..":
                # go back one level if not at root
                if stack:
                    # stack will be empty at root, non-empty otherwise
                    stack.pop()
            elif loc == ".":
                # the current dir, don't move
                continue
            else:
                # else loc is a real dir, append to stack
                stack.append(loc)
    # the canonical path should start with "/"
    return "/" + "/".join(stack)


test = "/a//b////c/d//././/.."
print(simplifyPath(test))

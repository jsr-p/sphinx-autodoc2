import astroid

node = astroid.extract_node("self.attribute = range(10)")

print(node)

print(list(node.get_children()))

list(node.get_children())[0].as_string()


node = astroid.extract_node(
    r"""
type RCMap = dict[tuple[int, int], str]
        """
)

childs = []
for c in node.get_children():
    print(type(c), c)
    childs.append(c)


print(childs[0].as_string())
print(childs[1].as_string())

import tree_sitter_python as tspython
from tree_sitter import Language, Parser, Tree, Node


py_language = Language(tspython.language())
py_parser = Parser(py_language)


def check_is_python(
    s: str,
    old_tree: Tree | None = None,
) -> tuple[bool, Tree]:
    # reusing trees is not faster :(
    # if old_tree:
    #     r = old_tree.root_node
    #     # minimal edit to the tree to make it reusable
    #     old_tree.edit(
    #         start_byte=r.start_byte,
    #         old_end_byte=r.end_byte,
    #         new_end_byte=r.end_byte,
    #         start_point=r.start_point,
    #         old_end_point=r.end_point,
    #         new_end_point=r.end_point,
    #     )
    #     tree = py_parser.parse(s.encode(), old_tree)

    tree = py_parser.parse(s.encode())
    return not tree.root_node.has_error, tree
class Layer():
    name = "Updown"

    required_packages = [
    ]

    sublimious_keymap = [
        # Bind <SPC>: to open command palette
        {"keys": ["<space>"], "command": "show_overlay",
         "description": "M–x", "args": {"overlay": "command_palette"}},
        # Use ag to search project
        {"keys": ["p", "g"], "command": "search_in_project",
         "description": "ag project"},
        # Close tab
        {"keys": ["b", "d"], "command": "close",
         "description": "close buffer"},
        # Close window / column
        {"keys": ["w", "d"], "command": "destroy_pane",
         "description": "close window", "args": {"direction": "self"}},
        # Alternate active window
        {"keys": ["w", "w"], "command": "focus_neighboring_group",
         "description": "last window"},
        {"keys": ["w", "b"], "command": "set_layout",
         "description": "balance columns",
         "args": {
            "cols": [0.0, 0.5, 1.0],
            "rows": [0.0, 1.0],
            "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
            }
        },
        # Comment helpers
        {"keys": [";", ";"], "command": "toggle_comment",
         "description": "comment", "args": {"block": False}},
        {"keys": ["c"], "category": "comment"},
        {"keys": ["c", "c"], "command": "toggle_comment",
         "description": "comment", "args": {"block": False}},
        {"keys": ["c", "b"], "command": "toggle_comment",
         "description": "block comment", "args": {"block": True}},
        # Move file around with <SPC> b + vim navigation keys
        {"keys": ["b", "h"], "command": "carry_file_to_pane",
         "description": "move buffer left", "args": {"direction": "left"}},
        {"keys": ["b", "j"], "command": "carry_file_to_pane",
         "description": "move buffer down", "args": {"direction": "down"}},
        {"keys": ["b", "k"], "command": "carry_file_to_pane",
         "description": "move buffer up", "args": {"direction": "up"}},
        {"keys": ["b", "l"], "command": "carry_file_to_pane",
         "description": "move buffer right", "args": {"direction": "right"}},
        # Files
        {"keys": ["f"], "category": "file"},
        {"keys": ["f", "f"], "command": "i_opener",
         "description": "open file"},
        {"keys": ["f", "u"], "command": "reopen_last_file",
         "description": "reopen tab"},
        {"keys": ["f", "n"], "command": "clone_file",
         "description": "new view"}
    ]

    sublime_keymap = []

    syntax_definitions = {}

    def init(self, config):
        pass

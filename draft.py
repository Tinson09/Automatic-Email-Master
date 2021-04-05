from spreadsheet import Row


class Draft:
    def __init__(self, email_template):
        self.email_template = str(email_template)

    def get_draft(self, row):
        return self.replace_dynamic_variables(row)

    def replace_dynamic_variables(self, row):
        key_set = row.get_key_set()
        draft = self.email_template
        for key in key_set:
            value = row.get_value()
            key = "{{" + key + "}}"
            draft = draft.replace(key, value)
        return draft

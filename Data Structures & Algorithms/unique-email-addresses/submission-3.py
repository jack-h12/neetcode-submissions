class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for i in range(len(emails)):
            final_email = ""
            seen_plus_symbol = False
            in_domain_section = False
            for j in range(len(emails[i])):
                if in_domain_section == True:
                    final_email += emails[i][j]
                elif emails[i][j] == "@":
                    final_email += emails[i][j]
                    in_domain_section = True
                elif seen_plus_symbol == True:
                    continue
                elif emails[i][j] == "+":
                    seen_plus_symbol = True
                elif emails[i][j] == ".":
                    continue
                else:
                    final_email += emails[i][j]

            if final_email not in email_set:
                email_set.add(final_email)

        return len(email_set)
        

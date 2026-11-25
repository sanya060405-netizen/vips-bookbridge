import os

html_path = r"C:\Users\SANYA\.gemini\antigravity\scratch\bookbridge\vips_report_printable.html"
with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

pos_ref = text.find('TC-01')
if pos_ref != -1:
    pos_start = text.rfind('<table', 0, pos_ref)
    pos_end = text.find('</table>', pos_ref) + 8

    new_table = """<table>
            <tr>
                <th style="width: 8%;">ID</th>
                <th style="width: 16%;">Module</th>
                <th style="width: 32%;">Test Scenario / Description</th>
                <th style="width: 24%;">Input / Preconditions</th>
                <th style="width: 20%;">Expected Result</th>
                <th style="width: 8%;">Status</th>
            </tr>
            <tr>
                <td><strong>TC-01</strong></td>
                <td>Authentication</td>
                <td>Student Registration</td>
                <td>Valid roll, email, password</td>
                <td>Account created; auto-login</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-02</strong></td>
                <td>Authentication</td>
                <td>Duplicate Roll Number Guard</td>
                <td>Existing roll <code>10517704426</code></td>
                <td>Blocked by UNIQUE constraint; alert</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-03</strong></td>
                <td>Authentication</td>
                <td>Duplicate Email Guard</td>
                <td>Existing student email</td>
                <td>Blocked; flash warning displayed</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-04</strong></td>
                <td>Authentication</td>
                <td>Valid Student Login</td>
                <td>Roll <code>10517704426</code> + <code>student123</code></td>
                <td>Password verified; session created</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-05</strong></td>
                <td>Authentication</td>
                <td>Invalid Password Login</td>
                <td>Roll <code>10517704426</code> + <code>wrongpass</code></td>
                <td>Auth rejected; error message</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-06</strong></td>
                <td>Authentication</td>
                <td>Unauthenticated Route Guard</td>
                <td>GET <code>/listings/create</code> without login</td>
                <td>Redirects to <code>/login</code> with warning</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-07</strong></td>
                <td>Authentication</td>
                <td>1-Click Demo Login</td>
                <td>GET <code>/demo-login/1</code> (Sanya)</td>
                <td>Session instantly initialized</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-08</strong></td>
                <td>Catalog</td>
                <td>Public Catalog Load</td>
                <td>HTTP GET <code>/</code></td>
                <td>HTTP 200; 8 seed books rendered</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-09</strong></td>
                <td>Search</td>
                <td>Keyword Search: Title</td>
                <td>Query <code>q=DBMS</code></td>
                <td>Displays Database System Concepts</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-10</strong></td>
                <td>Search</td>
                <td>Keyword Search: Author</td>
                <td>Query <code>q=Tanenbaum</code></td>
                <td>Displays Computer Networks</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-11</strong></td>
                <td>Filter</td>
                <td>Filter by Course Branch</td>
                <td>Select <code>course=MCA</code></td>
                <td>Displays only MCA syllabus books</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-12</strong></td>
                <td>Filter</td>
                <td>Filter by Exchange Type</td>
                <td>Select <code>type=Donate</code></td>
                <td>Displays free donation materials</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-13</strong></td>
                <td>Filter</td>
                <td>Filter by Availability Status</td>
                <td>Select <code>status=Available</code></td>
                <td>Excludes pending/completed items</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-14</strong></td>
                <td>Catalog</td>
                <td>View Book Detail Page</td>
                <td>GET <code>/listing/1</code></td>
                <td>HTTP 200; displays full book info</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-15</strong></td>
                <td>Listing</td>
                <td>Valid Book Creation</td>
                <td>Post 'Automata Theory' book</td>
                <td>Inserted; redirects to detail view</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-16</strong></td>
                <td>Listing</td>
                <td>Blank Title Validation</td>
                <td>Submit form with empty title</td>
                <td>Validation halts; alerts user</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-17</strong></td>
                <td>Request</td>
                <td>Submit Peer Interest Request</td>
                <td>Borrower submits note on book</td>
                <td>Saved with status 'Pending'</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-18</strong></td>
                <td>Request</td>
                <td>Self-Interest Request Guard</td>
                <td>Owner requests own book</td>
                <td>Blocked with alert notification</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-19</strong></td>
                <td>State</td>
                <td>Owner Accepts Request</td>
                <td>Owner submits status=Accepted</td>
                <td>Book shifts to 'Pending Handover'</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-20</strong></td>
                <td>State</td>
                <td>Owner Declines Request</td>
                <td>Owner submits status=Declined</td>
                <td>Book reverts to 'Available'</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-21</strong></td>
                <td>State</td>
                <td>Handover Finalization</td>
                <td>Owner clicks Confirm Handed Over</td>
                <td>Both book & request marked Done</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
            <tr>
                <td><strong>TC-22</strong></td>
                <td>Listing</td>
                <td>Listing Deletion Guard</td>
                <td>Owner deletes posted book</td>
                <td>Cascade delete; book removed</td>
                <td><span style="color:#059669;font-weight:bold;">PASS</span></td>
            </tr>
        </table>"""

    updated_text = text[:pos_start] + new_table + text[pos_end:]
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(updated_text)
    print("SUCCESS: Updated vips_report_printable.html with all 22 test cases!")
else:
    print("ERROR: TC-01 not found")

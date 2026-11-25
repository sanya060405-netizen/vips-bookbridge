"""
BookBridge Automated Verification Test Suite
"""
import unittest
from app import app
from database import get_db

class BookBridgeTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

    def test_homepage(self):
        """Test home catalogue loads and displays books."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'BookBridge', response.data)
        self.assertIn(b'Database System Concepts', response.data)
        self.assertIn(b'Computer Networks', response.data)
        self.assertIn(b'Sanya', response.data)
        print("[PASS] Homepage loaded with sample textbooks.")

    def test_search_and_filters(self):
        """Test search query and filter parameters."""
        response = self.client.get('/?q=DBMS')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Database System Concepts', response.data)

        # Filter by Lend
        response = self.client.get('/?type=Lend')
        self.assertEqual(response.status_code, 200)

        # Filter by Donate
        response = self.client.get('/?type=Donate')
        self.assertEqual(response.status_code, 200)
        print("[PASS] Search and filters functional.")

    def test_listing_detail(self):
        """Test viewing an individual book detail page."""
        response = self.client.get('/listing/1')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Database System Concepts', response.data)
        self.assertIn(b'Silberschatz', response.data)
        self.assertIn(b'Approved Campus Meeting Point', response.data)
        print("[PASS] Listing detail page loaded.")

    def test_guidelines_page(self):
        """Test safe handover guidelines page."""
        response = self.client.get('/guidelines')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Approved Campus Handover Guidelines', response.data)
        self.assertIn(b'Central Library Foyer', response.data)
        print("[PASS] Guidelines page loaded.")

    def test_vips_branding_and_redirect(self):
        """Test Vivekananda Institute of Professional Studies branding and legacy route redirect."""
        response = self.client.get('/about-project', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'VIVEKANANDA INSTITUTE OF PROFESSIONAL STUDIES', response.data)
        print("[PASS] Vivekananda Institute of Professional Studies branding verified and legacy route redirects cleanly.")

    def test_demo_login_and_create(self):
        """Test demo login and posting a new listing."""
        # Log in as Sanya (user_id 1)
        response = self.client.get('/demo-login/1', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Sanya', response.data)

        # Access create listing page
        response = self.client.get('/listings/create')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Post Book or Study Material', response.data)

        # Post a new book
        post_data = {
            'title': 'Automata Theory & Computability',
            'author': 'John E. Hopcroft',
            'subject': 'Theory of Computation',
            'course': 'MCA',
            'semester': 'Semester 2',
            'listing_type': 'Lend',
            'condition': 'Like New',
            'preferred_meeting_point_id': 1,
            'description': 'Textbook covering DFA, NFA, Context-Free Grammars, and Turing Machines.',
            'cover_image': 'bi-cpu'
        }
        response = self.client.post('/listings/create', data=post_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Automata Theory', response.data)
        print("[PASS] Authenticated user can create new listing.")

    def test_express_interest_flow(self):
        """Test borrower expressing interest in another student's book."""
        # Log in as Amit (user_id 4)
        self.client.get('/demo-login/4', follow_redirects=True)

        # Express interest in listing 2 (Computer Networks owned by Sanya)
        req_data = {
            'message': 'Hi Sanya, can I borrow Tanenbaum for next week lab quiz?',
            'meeting_point_id': 3,
            'proposed_duration': '10 Days'
        }
        response = self.client.post('/listing/2/express-interest', data=req_data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Interest request submitted', response.data)
        print("[PASS] Express-interest request submitted successfully.")

if __name__ == '__main__':
    unittest.main()

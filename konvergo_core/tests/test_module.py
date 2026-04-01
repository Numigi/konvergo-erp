# © 2025 Numigi (tm) and all its contributors (https://numigi.com)
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.tests.common import TransactionCase


class TestKonvergoCore(TransactionCase):
    """Test that konvergo_core module is properly installed."""

    def test_module_installed(self):
        """Test that the konvergo_core module is installed."""
        module = self.env["ir.module.module"].search([("name", "=", "konvergo_core")])
        self.assertTrue(module)
        self.assertEqual(module.state, "installed")

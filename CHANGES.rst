Changelog
=========


1.6 (unreleased)
----------------

- Nothing changed yet.


1.5 (2026-06-22)
----------------

- Fix ``AttributeError`` on Plone 6.2 / plone.app.contenttypes where
  ``can_edit`` became a read-only property; stop assigning to it in the view.
  [MrTango]
- Drop Python 2 leftovers (``six``, coding cookie) from the link consent view.
  [MrTango]


1.4 (2025-04-01)
----------------

- remove unnecessary dependency to plone.restapi
  [MrTango]


1.3 (2023-09-01)
----------------

- fix dependencies to make it work on Python 3
  [MrTango]


1.2 (2021-06-10)
----------------

- Improve link consent info view
  [MrTango]

- Enable link consent behavior for Link CT by default
  [MrTango]

1.1 (2021-06-07)
----------------

- Hide consent info text in link view, when the consent_info is not enabled
  [MrTango]


1.0 (2021-06-07)
----------------

- Initial release.
  [MrTango]

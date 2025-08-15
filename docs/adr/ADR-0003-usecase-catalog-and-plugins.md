# ADR-0003: Use-Case Catalog & Plugins
Status: **Accepted**

Decision: Use cases live in `packages/specs/usecases/<id>/` (profile + plan template + schema). Last-mile logic ships as signed artifacts (digests).

Consequences: Backend remains common; new use cases = new folder + new digest.


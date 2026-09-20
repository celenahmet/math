# math

Static source snapshot for `ahmetcelen.com.tr`, prepared from the production web root for Vercel.

## Vercel

Import the repository as an **Other** framework project. No build command is required; the repository root is the output directory.

The main HTML/CSS/JavaScript site and its images, PDFs, lesson pages, and static video pages are included.

## Known limitation

Vercel does not execute the legacy PHP files included in some QR, redirect, exam, and lesson paths. Those routes require a later static conversion or explicit Vercel redirects. The former WordPress `/blog` is intentionally excluded.

Production credentials, server logs, caches, old archives, and the unreferenced multi-gigabyte video/archive directories are excluded from this repository.

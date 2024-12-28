---
# Leave the homepage title empty to use the site title
title: ""
date: 2024-12-27
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  - block: resume-biography-3
    content:
      # Choose a user profile to display (a folder name within `content/authors/`)
      username: ricard-argelaguet
      text: ""
      # Show a call-to-action button under your biography? (optional)
      button:
        text: Download CV
        url: uploads/resume.pdf
    design:
      css_class: dark
      background:
        color: black
        image:
          # Add your image background to `assets/media/`.
          filename: stacked-peaks.svg
          filters:
            brightness: 1.0
          size: cover
          position: center
          parallax: false
  - block: collection
    id: publications
    content:
      title: Publications
      filters:
        folders:
          - publication
        featured_only: false
    design:
      view: article-grid
      columns: 2
  # - block: collection
  #   content:
  #     title: Recent Publications
  #     text: ""
  #     filters:
  #       folders:
  #         - publication
  #       exclude_featured: false
    design:
      view: citation
  - block: collection
    id: talks
    content:
      title: Talks
      filters:
        folders:
          - talks
    design:
      view: card
      columns: 1
  - block: collection
    id: teaching
    content:
      title: Teaching
      filters:
        folders:
          - teaching
    design:
      view: card
      columns: 1
  # - block: collection
  #   id: supervision
  #   content:
  #     title: Supervision
  #     filters:
  #       folders:
  #         - supervision
  #   design:
  #     view: compact
  #     columns: 1

---

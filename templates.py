song = """
<!-- wp:heading {"level":[HEADING_LEVEL]} -->
<h[HEADING_LEVEL] class="wp-block-heading">[SONG_NAME]</h[HEADING_LEVEL]>
<!-- /wp:heading -->

<!-- wp:embed {"url":"[YOUTUBE_URL]","type":"video","providerNameSlug":"youtube","responsive":true,"className":"wp-embed-aspect-16-9 wp-has-aspect-ratio"} -->
<figure class="wp-block-embed is-type-video is-provider-youtube wp-block-embed-youtube wp-embed-aspect-16-9 wp-has-aspect-ratio"><div class="wp-block-embed__wrapper">
[YOUTUBE_URL]
</div></figure>
<!-- /wp:embed -->
"""

spacer = """
<!-- wp:spacer {"height":"[HEIGHT]"} -->
<div style="height:[HEIGHT]" aria-hidden="true" class="wp-block-spacer"></div>
<!-- /wp:spacer -->
"""

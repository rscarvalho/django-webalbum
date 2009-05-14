===========
README FILE
===========

++++++++++++
Introduction
++++++++++++

django-webalbum offers a simple way to manage picture albums, providing a configurable environment, 
intended to provide a full-featured web album component for your django applications.


++++++++++++
Installation
++++++++++++

The installation process is very simple. Just run ``python setup.py install`` in the terminal, or put the django-webalbum source
folder into your ``PYTHONPATH`` environment variable.


+++++++++++++
Configuration
+++++++++++++

There are some configuration variables you can use to customize the behavior of your application.

+------------------------------------+---------------------------------+----------------------+------------------------+
| Variable Name                      | Meaning                         | Acceptable values    | Default Value          |
+====================================+=================================+======================+========================+
| ALBUM_DEFAULT_EXTENSION            | Default Extension for images    | any file extension   | "jpg"                  |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_IMAGE_SIZE                   | A tuple containing the album    |  a tuple of          | (480, 320)             |
|                                    | image sizes (width, height)     |  integers            |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_ALBUM_THUMBNAIL_SIZE         | A tuple containin the album     |  a tuple of          | (180, 124)             |
|                                    | thumbnail size for album cover  |  integers            |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_PHOTO_THUMBNAIL_SIZE         | A tuple containing the album    |  a tuple of          | (80, 80)               |
|                                    | thumbnail size for album images |  integers            |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_COVER_SIZE                   | Size of album's cover image     |  a tuple of          | (150, 150))            |
|                                    |                                 |  integers            |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_COVER_THUMB_SIZE             | A tuple containing the album's  |  a tuple of          |  ``None``              |
|                                    | cover thumbnail size (if any)   |  integers, or None   |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_OVER_COVER                   | The path for an image that will | a path relative to   | ``None``               |
|                                    | be pasted over the cover image  | to MEDIA_ROOT        |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_PUT_WATERMARK                | Set to True if you want to use  | ``True``/``False``   | ``False``              |
|                                    | a watermark on the image        |                      |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_WATERMARK                    | The path for the watermark file | a valid absolute     | settings.MEDIA_ROOT +  |
|                                    |                                 | path to the file     | "images/watermark.png" |
+------------------------------------+---------------------------------+----------------------+------------------------+ 
| ALBUM_WATERMARK_POSITION           | The position of the watermark,  | bottomleft, center   | "bottomleft"           |
|                                    | relative to the image           | bottomright, topleft |                        |
|                                    |                                 | topright             |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_WATERMARK_ALPHA              |  *NOT IMPLEMENTED*              | *NOT IMPLEMENTED*    | 0.7                    |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_CROP_ORIENTATION             |  *NOT IMPLEMENTED*              | *NOT IMPLEMENTED*    | "center"               |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_ALBUMS_PER_PAGE              | The amount of albums per page   | any integer          | 8                      |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_PHOTOS_PER_PAGE              | The amount of photos per page   | any integer          | 9                      |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_PORTRAIT_SIZE                | Set to true if photos can be in | ``True``/``False``   | ``False``              |
|                                    | portrait orientation            |                      |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_HAS_HIGHLIGHT                | Set to True if your albums have | ``True``/``False``   | ``False``              |
|                                    | highlight pictures              |                      |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_HIGHLIGHT_SIZE               | A tuple indicating the album's  | a tuple of           | (156, 314)             |
|                                    | higlight size (if any)          | integers             |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_HIGHLIGHT_THUMB_SIZE         | A tuple indicating the album    | a tuple of           | (240, 256)             |
|                                    | highlight's thumbnail size (if  | integers             |                        |
|                                    | any)                            |                      |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_HIGHLIGHT_WATERMARK          | The path for a watermark to     |  a valid path,       | ``None``               |
|                                    | put on the higlight picture     |  relative to         |                        |
|                                    | (if any)                        |  ``MEDIA_ROOT``      |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_HIGHLIGHT_WATERMARK_POSITION |  *NOT IMPLEMENTED*              |  *NOT IMPLEMENTED*   | "bottomleft"           |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_HAS_PHOTOGRAPHER             | Set to True if you want to      | ``True``/``False``   | ``False``              |
|                                    | include a photographer for your |                      |                        |
|                                    | albums                          |                      |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_PAGE_NEXT                    | A text for representing "Next   | any string (HTMLs    | "&raquo;"              |
|                                    | page" element in album list     | are OK)              |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_PAGE_PREV                    | A text for representing "Prev   | any string (HTMLs    | "&laquo;"              |
|                                    | page" element in album list     | are OK)              |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_PAGE_NO_NEXT                 | A text to render if there is no | any string (HTMLs    | ""                     |
|                                    | next page in album list.        | are OK)              |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_PAGE_NO_PREV                 | A text to render if there is no | any string (HTMLs    | ""                     |
|                                    | previous page in album list.    | are OK)              |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_PICTURE_PAGE_NEXT            | A text for representing "Next   | any string (HTMLs    | "&raquo;"              |
|                                    | page" element in photo list     | are OK)              |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+
| ALBUM_PICTURE_PAGE_PREV            | A text for representing "Prev   | any string (HTMLs    | "&laquo;"              |
|                                    | page" element in photo list     | are OK)              |                        |
+------------------------------------+---------------------------------+----------------------+------------------------+


+++++++
Contact
+++++++

You can contact me by e-mail:

Rodolfo Carvalho <rodolfo@rcarvalho.eti.br>
import flet as ft

# define a song class as our model
class Song(object):
    def __init__(self, song_name: str, artist_name: str, audio_path: str, img_path: str):
        super(Song, self).__init__()
        self.song_name: str = song_name
        self.artist_name: str = artist_name
        self.audio_path: str = audio_path
        self.img_path: str = img_path

    # define a proeprties for this calss to access each atribute

    @property
    def name(self):
        return self.song_name

    @property
    def artist(self):
        return self.artist_name

    @property
    def path(self):
        return self.audio_path

    @property
    def path_img(self):
        return self.img_path


# next, define a directory class where we store individulae songs
class AudioDirectory(object):
    # fill out as many songs as you want
    playlist: list = [
        Song(
            song_name='Stay With Me',
            artist_name='Miki Matsubara',
            audio_path='0.mp3',
            img_path='0.png',
        ),
        Song(
            song_name='Suzuke',
            artist_name='Toaka',
            audio_path='1.mp3',
            img_path='1.png',
        ),
    ]





# our first page/view is the playlist
class Playlist(ft.View):
    def __int__(self, page: ft.Page):
        super(Playlist, self).__init__(
            route='/playlist',
            horizontal_alignment='center'
        )

        self.page = page
        self.playlist: list[Song] = AudioDirectory.playlist

        self.controls = [
            ft.Row(
                [
                    ft.Text('Playlist', size=21, weight='bold', color='black'),

                ],
                alignment='center'
            ),
            ft.Divider(height=10, color='transparent')
        ]

def main(page: ft.Page):
    page.theme_mode = ft.ThemeMode.LIGHT

    def router(route):
        page.views.clear()

        if page.route == '/playlist':
            playlist = Playlist(page)
            page.views.append(playlist)

        page.update()

    page.on_route_change = router
    page.go('/playlist')


    page.on_route_change = router
    page.go('/playlist')


ft.app(target=main, assets_dir='assets')
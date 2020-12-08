import pdb
from models.artist import Artist
from models.album import Album
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist('Lee Perry')
artist_repository.save(artist_1)

artist_2 = Artist('Chinese Man')
artist_repository.save(artist_2)

artist_repository.select(artist_1.id)
artist_repository.select_all()

album_1 = Album('Black Arc','dub',artist_1)
album_repository.save(album_1)
album_2 = Album('Rise Again','dub', artist_1)
album_repository.save(album_2)
album_3 = Album('Racing with the Sun','hiphop', artist_2)
album_repository.save(album_3)
album_4 = Album('The Journey','hiphop', artist_2)
album_repository.save(album_4)
album_repository.select(album_1.id)


res = album_repository.select_all()
for album in res:
    print(album.__dict__)
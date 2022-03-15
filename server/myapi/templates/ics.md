{% load film_tags %}

{{ film.title }} - {{ film.director }}

**Pays** : {{ film.origin_country }}  
**Durée** : {{ film.duration|movie_duration }} 
**Année** : {{ film.release_year }}  
{% color_display film.is_in_color %}
{{ film.movie_format }} . {{ film.language_subtitles }}  
**Avec** : {% list_actors film.actors %} 

Plus d'informations sur [notre site Internet](http://www.cineclub.ens.fr/category/seances/), [facebook](https://www.facebook.com/cineclub.ensulm), [instagram](https://www.instagram.com/cineclubens/) ou via la [newsletter](https://lists.ens.psl.eu/wws/info/cineclub-informations)

Comme d’habitude, l’entrée coûte {{ prices.one_cof }}€ pour les membres du COF.
L’entrée est gratuite pour les membres du Programme Étudiant⋅e⋅s Invité⋅e⋅s.

# Page_web_ROS2

Page web ROS2


Simple pub et sub ros2 mais avec en plus la fonctionnalité de recopier ce que reçoit le sub sur une page web! 
Attention à bien mettre l'adresse IP de votre machine

![image](https://github.com/anasdtp/Page_web_ROS2/assets/116441391/ee81cb16-319e-4eb2-af3c-9c249fc86066)

La page sera donc à 
```
http://votre_adr_ip:8080/
```

Si vous voulez rajouter une page data par ex, rajouter aprés home:
```
@app.route('/data', methods=['GET'])
def get_data():
    # Code pour récupérer les données à partir de sources locales (fichiers, bases de données, etc.)
    return "Données de la page web"
```


Aller dans le workspace ros2 puis :
```
cd src/
git clone https://github.com/anasdtp/pg_web_ros
cd ..
colcon build --packages-select pg_web_ros
```
Dans un autre terminal, aller dans le workspace ros2 puis :
```
source install/setup.bash
ros2 run pg_web_ros listener
```
Vous pouvez maintenant aller ouvrir la page http://votre_adr_ip:8080/ dans un navigateur
Ouvrir un autre terminal, aller dans le workspace ros2 puis :
```
source install/setup.bash
ros2 run pg_web_ros talker
```
Vous pouvez maintenant voir les trames arrivant du pub au sub via la page web en rafraichissant la page web plusieurs fois.


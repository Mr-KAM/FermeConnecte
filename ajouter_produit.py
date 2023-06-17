from deta import *  # pip install deta
from dotenv import load_dotenv
from _database import *
load_dotenv()

cle_ferme_connecte = os.environ["cle_ferme_connecte"]
deta = Deta(cle_ferme_connecte)

prod= deta.Base("produits")
prod_img=deta.Drive("produit")
datas=[
    {
    "key": "lapin_entier",
    "categorie": "Viande,Animaux",
    "description": "Le lapin domestique est un lapin européen, qui a été domestiqué pour l'alimentation humaine en Europe occidentale, au Moyen Âge, une époque relativement récente comparée à d'autres animaux domestiques. Les lapins de clapier sont de petits mammifères herbivores qui diffèrent très peu de l'espèce souche, classée dans l'ordre des Lagomorphes, la famille des léporidés et le genre Oryctolagus. À l'origine, le lapin européen est élevé en semi-liberté dans de vastes espaces clos comme « lapin de garenne », afin d'assurer notamment la production de laurices durant la période de carême. Depuis lors, de très nombreuses races de lapins ont été créées dans le cadre de l'élevage sélectif effectué par les humains, en fonction de l'usage auquel la cuniculture les destine. Au début du xxe siècle on recense plus de 100 races de lapins domestiques.",
    "prix": 5000,
    "quantite": 10,
    "titre": "Lapin entier",
    "unite": "Tête"
},
{
    "key": "pondeuse_entier",
	"categorie": "Viande,Animaux",
	"description": "La pondeuse est une poule spécialement élevée pour la production d'œufs. Elle appartient à la famille des gallinacés et est élevée dans des élevages avicoles. Les pondeuses sont sélectionnées pour leur capacité à produire un grand nombre d'œufs tout au long de leur vie. Elles sont généralement nourries avec une alimentation spéciale riche en protéines pour favoriser la ponte. Les œufs produits par les pondeuses sont largement consommés dans le monde entier et constituent une source importante de protéines. Les pondeuses entières sont parfois utilisées dans la cuisine pour préparer des plats à base de poulet. Elles sont appréciées pour leur chair tendre et leur saveur délicate.",
	"prix": 6000,
	"quantite": 8,
	"titre": "Pondeuse entière",
	"unite": "Tête"
}, 
{
    "key": "tomate",
    "categorie": "Légume,Plantes",
    "description": "La tomate est un fruit comestible originaire d'Amérique du Sud, largement cultivé comme légume dans de nombreuses régions du monde. Il existe de nombreuses variétés de tomates, allant des petites tomates cerises aux grosses tomates beefsteak. Les tomates sont riches en vitamines et en antioxydants, ce qui en fait un ingrédient populaire dans de nombreux plats et salades. Elles peuvent être consommées crues, cuites ou transformées en sauces, jus et conserves. Les tomates sont cultivées dans des jardins, des serres et des exploitations agricoles à grande échelle.",
    "prix": 2000,
    "quantite": 30,
    "titre": "Tomate",
    "unite": "Kilogramme"
},
{
    "key": "laitues",
    "categorie": "Légume,Plantes",
    "description": "La laitue est une plante herbacée annuelle appartenant à la famille des Astéracées. Elle est largement cultivée pour ses feuilles comestibles et constitue l'un des légumes-feuilles les plus populaires. Il existe différentes variétés de laitue, telles que la laitue romaine, la laitue iceberg et la laitue pommée. Les laitues sont souvent utilisées dans les salades, les sandwichs et les wraps. Elles sont riches en vitamines et en minéraux et contribuent à une alimentation saine et équilibrée.",
    "prix": 1500,
    "quantite": 20,
    "titre": "Laitues",
    "unite": "piece"
},
{
	"key": "concombre",
	"categorie": "Légume",
	"description": "Le concombre est un légume appartenant à la famille des cucurbitacées. Il est caractérisé par sa forme allongée et sa peau verte lisse. Le concombre est largement cultivé et consommé dans de nombreuses régions du monde. Il est apprécié pour son goût rafraîchissant et sa texture croquante. Le concombre est souvent consommé cru, en salade ou en accompagnement de plats. Il est également utilisé pour préparer des jus, des smoothies ou des pickles. En plus de son aspect culinaire, le concombre est réputé pour ses bienfaits hydratants et sa teneur en vitamines et minéraux.",
	"prix": 2000,
	"quantite": 20,
	"titre": "Concombre",
	"unite": "Kilogramme"
},
{
	"key": "agoutis_entier",
	"categorie": "Viande,Animaux",
	"description": "Les agoutis sont des petits mammifères appartenant à la famille des Dasyproctidés. Ils se trouvent principalement en Amérique centrale et en Amérique du Sud. Les agoutis sont connus pour leur apparence similaire à celle des cochons d'Inde, avec un corps robuste, de courtes pattes et une queue mince. Ils sont herbivores et se nourrissent principalement de fruits, de graines et de végétaux. Les agoutis sont souvent chassés pour leur viande, qui est considérée comme une source de protéines dans certaines régions. Leur viande est appréciée pour sa saveur délicate et est utilisée dans la cuisine locale. En raison de la chasse excessive et de la destruction de leur habitat, certaines espèces d'agoutis sont menacées ou en voie de disparition.",
	"prix": 7000,
	"quantite": 5,
	"titre": "Agoutis entier",
	"unite": "Tête"
},
{
	"key": "poulet_de_chair_entier",
	"categorie": "Viande,Animaux",
	"description": "Le poulet de chair est une volaille élevée spécifiquement pour sa viande. Il appartient à la famille des gallinacés et est largement consommé dans de nombreux pays. Les poulets de chair sont élevés dans des fermes avicoles où ils sont nourris avec une alimentation spéciale pour favoriser une croissance rapide. Ils sont abattus à un âge relativement jeune, généralement entre 6 et 8 semaines, pour obtenir une viande tendre et savoureuse. Le poulet de chair entier est souvent utilisé dans la cuisine pour préparer une variété de plats tels que rôtis, grillades ou cuissons au four. Il est apprécié pour sa chair juteuse et sa polyvalence culinaire.",
	"prix": 8000,
	"quantite": 12,
	"titre": "Poulet de chair entier",
	"unite": "Tête"
},
{
	"key": "Cochon_entier",
	"categorie": "Viande,Animaux",
	"description": "Le cochon, également connu sous le nom de porc, est un mammifère domestique élevé pour sa viande. Il fait partie de la famille des suidés et est largement élevé dans de nombreuses régions du monde pour sa chair savoureuse. Les cochons sont élevés dans des fermes appelées élevages porcins. Ils sont généralement abattus à un âge adulte pour obtenir différents types de viande, tels que le porc frais, le jambon, le bacon, les saucisses, et bien d'autres produits porcins. La viande de cochon est appréciée pour sa saveur et sa texture, et elle est utilisée dans de nombreuses cuisines traditionnelles et contemporaines.",
	"prix": 12000,
	"quantite": 8,
	"titre": "Cochon",
	"unite": "Tête"
},
{
	"key": "cabri_entier",
	"categorie": "Viande,Animaux",
	"description": "Le cabri est un jeune de la chèvre, généralement âgé de moins d'un an. Sa viande est prisée dans de nombreuses cuisines du monde. Le cabri entier, c'est-à-dire le cabri non découpé, est souvent utilisé dans des plats traditionnels et des rôtis. Sa chair est tendre et savoureuse, avec une saveur distincte. Le cabri est souvent apprécié pour sa viande maigre et sa texture délicate. Il peut être préparé de différentes manières, que ce soit rôti, grillé, braisé ou cuisiné dans des plats en sauce. Le cabri entier est une option idéale pour ceux qui souhaitent cuisiner un repas complet à base de viande de cabri.",
	"prix": 8000,
	"quantite": 5,
	"titre": "Cabri entier",
	"unite": "Tête"
},
{
	"key": "lait_de_vache",
	"categorie": "Produits laitiers",
	"description": "Le lait de vache est un liquide produit par les vaches femelles. Il est largement consommé dans de nombreux pays et utilisé comme ingrédient dans de nombreuses recettes et produits laitiers. Le lait de vache est riche en nutriments tels que le calcium, les protéines, les vitamines et les minéraux. Il est souvent consommé tel quel, utilisé dans la préparation de boissons lactées, de yaourts, de fromages et d'autres produits laitiers. Le lait de vache entier est obtenu sans retirer la matière grasse naturelle présente dans le lait, ce qui lui confère une texture crémeuse et un goût plus riche. Il est utilisé dans de nombreuses recettes culinaires pour apporter de l'onctuosité et de la saveur.",
	"prix": 3000,
	"quantite": 20,
	"titre": "Lait de vache entier",
	"unite": "Litre"
}]

def add_datas(prod,datas):
    for data in datas:
        add_data(prod,data) 
    return True  
if __name__ == "__main__":
    add_datas(prod,data)


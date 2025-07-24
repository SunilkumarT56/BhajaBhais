import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "your_project_name.settings")
django.setup()

from myapp.models import NameSet

def run():
    name_list = "Sasikumar Veluchamy (C), Prithiv (VC), Vishanth, Naufel Mahmood, Sivarajan, Hari Shankar, Santhosh M, Santhosh, Lakshmanan, Prabu, Giridharan, Gowtham, Kirpesh, Nakul, Mohana Krishnan, Vignesh Dharsan, Arjun, Manoj, Kowtham, Sunder Perumal, John, Krishna, Kowshik, Rajkumar, Abishek, Sibi, Siddhu, Ramprasad, Santhosh V, Sharma, Gobinath, Sri Vishnu"

    NameSet.objects.create(name=name_list)
    print("✅ Name set with id=1 added!")

if __name__ == "__main__":
    run()

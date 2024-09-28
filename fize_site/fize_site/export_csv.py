import csv
from auth_app.models import Administrateur, Salle, Teacher, ResponsableFiliere, Filiere, Matiere, Student, Classe, Note

def export_to_csv():
    with open('mld.csv', 'w', newline='') as csvfile:
        fieldnames = ['Model', 'Field', 'Type', 'Options']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()

        models = [Administrateur, Salle, Teacher, ResponsableFiliere, Filiere, Matiere, Student, Classe, Note]

        for model in models:
            for field in model._meta.fields:
                writer.writerow({
                    'Model': model.__name__,
                    'Field': field.name,
                    'Type': field.get_internal_type(),
                    'Options': field.null
                })

if __name__ == "__main__":
    export_to_csv()

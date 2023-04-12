from Automate import create_dto, create_irepository, create_irepository_manager, create_irepository_implementation, \
    create_repository_manager

model_path = r"C:\Users\mahto\OneDrive\Documents\MAIN LAB\V7\CNET_V7_Entities\DataModels"
# create_dto_dir_path = r"C:\Users\mahto\OneDrive\Documents\MAIN LAB\V7\CNET_V7_Domain\Domain"
create_irepository_root_path = r"C:\Users\mahto\Desktop\test"
create_dto_dir_path = r'C:\Users\mahto\Desktop\test'

irepository_manager_create_path = r'C:\Users\mahto\Desktop\test\IRepositoryManager.cs'
repository_manager_create_path = r'C:\Users\mahto\Desktop\test\RepositoryManager.cs'

create_irepository_implementation_root = r'C:\Users\mahto\Desktop\test'

if __name__ == '__main__':
    # create_dto(model_path, create_dto_dir_path)

    # create_irepository(model_path, create_irepository_root_path)

    # create_irepository_implementation(model_path, create_irepository_implementation_root)

    # create_irepository_manager(model_path, irepository_manager_create_path)
    create_repository_manager(model_path, repository_manager_create_path)

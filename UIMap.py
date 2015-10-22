
PublicPageMap = dict (UsernameFieldXpath	= "//input[@name='username']",
					   PasswordFieldXpath	= "//input[@name='password']",
					   LoginButtonNameXpath	= "//button[.='Log in']",
					   BlogButtonsXpath		= "//a[.='Blog']",
					   NewsEmailfieldXpath	= "//input[@id='email']"
)

ProHomepage = dict	(GlobalSearchBarXpath	= "//input[@id='gc-topnav-search']",
					 AddExerciseButtonXpath = "//a[@class='btn btn-link gc-show-add-exercise-modal']",
					 ExerciseFirstRadioBtn	= "(//input[@type='checkbox'])[2]",
					 EWPDeleteButton		= "//span[@class='fa fa-trash']"
)

ProSidebar	= dict  (ExercisesButtonLink	= "//span[.='EXERCISES']"
)

ModalPopupMap = dict (AddExercisePopup		= "//*[@id='gc-modal-region']//input[@class='form-control']",
					  AddExerciseButton 	= "//*[@id='gc-modal-region']//button[@class='btn btn-primary gc-add-personal-best-add']",
					  Deletebutton			= "//button[@class='btn btn-danger confirm'][@data-dismiss='modal'][.='Delete']"
)
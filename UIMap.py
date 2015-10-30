
PublicPageMap = dict (UsernameFieldXpath	= "//input[@name='username']",
					   PasswordFieldXpath	= "//input[@name='password']",
					   LoginButtonNameXpath	= "//button[.='Log in']",
					   BlogButtonsXpath		= "//a[.='Blog']",
					   NewsEmailfieldXpath	= "//input[@id='email']"
)

ProHomepage = dict	(GlobalSearchBarXpath	= "//input[@id='gc-topnav-search']",
					 AddEWPButtonXpath 		= "//a[@class='btn btn-link gc-show-add-exercise-modal']",
					 ExerciseFirstRadioBtn	= "(//input[@type='checkbox'])[2]",
					 EWPDeleteButton		= "//span[@class='fa fa-trash']",
					 ExerciseDescField		= "//textarea[@placeholder='Add description here...']",
					 WorkoutDescField		= "//textarea[@class='gc-workout-description-editor gc-description-editor form-control'][@placeholder='Start typing a description here...']",
					 ProgramDescField		= "//textarea[@class='gc-program-description-editor gc-description-editor form-control'][@placeholder='Start typing a description here...']",
					 
					 EWPnameField			= "//span[@contenteditable='true']"

)

ProSidebar	= dict  (ExercisesButtonLink	= "//span[.='EXERCISES']",
					 WorkoutButtonLink		= "//span[.='WORKOUTS']",
					 ProgramButtonLink		= "//span[.='PROGRAMS']",

					 ExerciseDropdown		= "//region[@data-name='exercises']//*[@class='gc-menu-item-arrow toggle-it']",
					 WorkoutDropdown		= "//region[@data-name='workout_templates']//*[@class='gc-menu-item-arrow toggle-it']"
					 
)

ModalPopupMap = dict (AddExercisePopup		= "//*[@id='gc-modal-region']//input[@class='form-control']",
					  AddExerciseButton 	= "//*[@id='gc-modal-region']//button[@class='btn btn-primary gc-add-personal-best-add']",
					  Deletebutton			= "//button[@class='btn btn-danger confirm'][@data-dismiss='modal'][.='Delete']"
)
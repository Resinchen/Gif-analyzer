# Gif-analyzer
Анализатор gif-изображений

<hr>
ОПИСАНИЕ ФАЙЛОВ:

	РАСШИРЕНИЯ:
		AddonApp - расширение приложения
		AddonComment - расширение комментария
		AddonGraphicalControl - расширение графического контроля

	CgifAnalis - консольная версия программы 
	gifAnalis - графическая версия программы
	
	MainFrame - главная структура, объединяющая основные блоки gif и блоки изображений

	Header - заголовок
	DescriptorLogicScreen - дескиптор логического экрана
	DescriptorImage - дескриптор изображения
	Frame - блок с изображением (вместе с блоками расширений)

	GUI - описание графики
	
	Info - структура, в которой хранится собираемая информация
	
	Palette - палитра
	TrinityColor - цвет в формате RGB
  
  <hr>
  ИСПОЛЬЗОВАНИЕ:

    формат запуска консольной версии: python CgifAnalis.py <input file>

    формат запуска графической версии: python gifAnalis.py

    вызов справки: python CgifAnalis.py -h

    пример запуска: python CgifAnalis.py example.gif

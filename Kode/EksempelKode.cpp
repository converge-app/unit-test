void * writer(void * sharedPtr)
{
	// Cast paramter to Vector pointer
	Vector * sharedVectorPtr = static_cast<Vector*>(sharedPtr);

	int maxNo = 10;  // Set number of times to compare

	pthread_t threadID = pthread_self();  // Get thread ID

	for (int i = 0; i < maxNo; ++i)
	{
		// Check Vector with thread ID
		if(sharedVectorPtr->setAndTest(threadID) == false)
			std::cout << "Error in thread number: " << threadID << std::endl;

		sleep(1);
	}

	return nullptr;
}

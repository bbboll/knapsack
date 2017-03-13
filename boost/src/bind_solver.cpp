#include "knapsack.hpp"
#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>

using namespace boost::python;

// expose python module libknapsack
BOOST_PYTHON_MODULE(libknapsack) 
{
	class_<ItemList>("ItemList")
		.def(vector_indexing_suite<ItemList>());

	class_<Knapsack>("Knapsack")
		.def("setCapacity", &Knapsack::setCapacity)
		.def("addItem", &Knapsack::addItem)
		.def("solve", &Knapsack::solve);
};
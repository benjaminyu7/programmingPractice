// See https://aka.ms/new-console-template for more information

using System.Data;
using System.Text;
using Algorithms;
using DataStructures;
using DataStructures.Factory;

var removeDuplicates = new RemoveDuplicates();

TreeNode head = new TreeNode(1, new TreeNode(2), new TreeNode(3, new TreeNode(4), new TreeNode(5)));
var output = BinaryTreeSerialize.Serialize(head);
Console.WriteLine(output);
var deserializeOutput = BinaryTreeSerialize.Deserialize("1,2,3,1002,1002,4,5,6,7");
output = BinaryTreeSerialize.Serialize(deserializeOutput);
Console.WriteLine(output);
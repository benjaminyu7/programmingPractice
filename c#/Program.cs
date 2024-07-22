// See https://aka.ms/new-console-template for more information

using System.Data;
using System.Reflection.Metadata;
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

MatchSubstringAfterReplacement sol = new MatchSubstringAfterReplacement();

char[][] mappings = new char[][] 
{ 
    new char[]{'a','b'},
    new char[]{'c','d'},
    new char[]{'c','a'},
    new char[]{'b','a'},
    new char[]{'b','c'},
} ;
Dictionary<char,HashSet<char>> graph = sol.CreateGraph(mappings);
foreach (var entry in graph)
{
    Console.WriteLine($"Key: {entry.Key} Value: {string.Join(",", entry.Value)}");
}

Console.WriteLine("PossibleChars");
string sub = "abc";
Dictionary<char, HashSet<char>> possibleChars = sol.PossibleChars(sub, graph);
foreach (var entry in possibleChars)
{
    Console.WriteLine($"Key: {entry.Key} Value: {string.Join(",", entry.Value)}");
}

Console.WriteLine("MatchSubstring");
Console.WriteLine(sol.MatchSubstring("abcd", sub, possibleChars));
Console.WriteLine(sol.MatchSubstring("dabc", sub, possibleChars));

Console.WriteLine(sol.MatchReplacement("dbac", "abd", mappings));
mappings = new char[][] 
{ 
    new char[]{'e','3'},
    new char[]{'t','7'},
    new char[]{'t','8'}
};
Console.WriteLine(sol.MatchReplacement("fool3e7bar", "leet", mappings));

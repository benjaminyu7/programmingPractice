using System.Dynamic;
using System.Collections.Generic;

namespace Algorithms
{
    public class MatchSubstringAfterReplacement
    {
        public MatchSubstringAfterReplacement()
        {
        }

        public bool MatchReplacement(string s, string sub, char[][] mappings)
        {
            Dictionary<char,HashSet<char>> graph = CreateGraph(mappings);
            foreach (var entry in graph)
            {
                Console.WriteLine($"Key: {entry.Key} Value: {string.Join(",", entry.Value)}");
            }

            Console.WriteLine("PossibleChars");
            Dictionary<char, HashSet<char>> possibleChars = PossibleChars(sub, graph);
            foreach (var entry in possibleChars)
            {
                Console.WriteLine($"Key: {entry.Key} Value: {string.Join(",", entry.Value)}");
            }

            return MatchSubstring(s, sub, possibleChars);
        }

        public Dictionary<char, HashSet<char>> CreateGraph(char[][] mappings)
        {
            Dictionary<char, HashSet<char>> graph = new Dictionary<char, HashSet<char>>();
            for (int i = 0; i < mappings.Length; i++)
            {
                char key = mappings[i][0];
                char value = mappings[i][1];
                if (!graph.ContainsKey(key))
                {
                    graph[key] = new HashSet<char>();
                }
                graph[key].Add(value);
            }
            return graph;
        }
        
        public Dictionary<char, HashSet<char>> PossibleChars(string sub, Dictionary<char,HashSet<char>> graph)
        {
            Dictionary<char, HashSet<char>> possibleChars = new Dictionary<char, HashSet<char>>();
            foreach (char letter in sub)
            {
                HashSet<char> visited = new HashSet<char>();
                if (!possibleChars.ContainsKey(letter))
                {
                    possibleChars[letter] = new HashSet<char>(){letter};
                    if(graph.ContainsKey(letter))
                    {
                        List<HashSet<char>> queue = new List<HashSet<char>>
                        {
                            graph[letter]
                        };
                        visited.Add(letter);
                        while(queue.Count > 0)
                        {
                            foreach(char c in queue[0])
                            {
                                if(!visited.Contains(c))
                                {
                                    visited.Add(c);
                                    possibleChars[letter].Add(c);
                                    if (possibleChars.ContainsKey(c))
                                    {
                                        queue.Add(possibleChars[c]);
                                    }
                                }
                            }
                            queue.RemoveAt(0);
                        }
                    }
                    
                }
            }
            return possibleChars;
        }

        public bool MatchSubstring(string s, string sub, Dictionary<char,HashSet<char>> possibleChars)
        {
            for(int i = 0; i < s.Length; i++)
            {
                int j = 0;
                int subIndex = 0;
                while(
                    i+j < s.Length 
                    && subIndex < sub.Length 
                    && possibleChars[sub[subIndex]].Contains(s[i+j])
                )
                {
                    j++;
                    subIndex++;
                }
                if(subIndex == sub.Length)
                {
                    return true;
                }
            }
            return false;
        }
    }
}
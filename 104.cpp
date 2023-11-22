/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int maxDepth(TreeNode* root) {
    // Approach1: c++ one liner
        return root ? 1 + max(maxDepth(root->left), maxDepth(root->right)) : 0;

    // Approach2: delegate to left & right branch
    //     if(root==NULL){
    //         return 0;
    //     }
    //     else{
    //         return max(maxDepth(root->left),maxDepth(root->right))+1;
    //     }
    }
};
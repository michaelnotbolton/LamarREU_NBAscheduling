clc; clear all
%% eastern/western conf intra %%
% genereate pairings of vertex 1/2 with infinity (portal)
A = 2:8;
B = 15:-1:9;
M = zeros(1, 7);
answers = [A', B'];
for j = 1:15
    M(j,:) = A; M(j+1,:)=B;
    A = A+1; B = B+1;
    for i =1:7
        if A(i)==16 
           A(i) = 1;
        end
        if B(i)==16
           B(i) = 1;
        end
        answers = [answers ; [A(i) B(i)]];
    end
end
% the output answer set contains 105+7 games total
% trunc_answer uses the first 105 games as it represents vertex 1 paired
% with infinity
% shifted index uses the last 105 games as it represents vertex 2 paired
% with infinity
[m,n] = size(answers);

conf = ['east';'west']; 
h_or_a = ['home';'away'];

%% home-away
% "answers" have a repeated night of games in the end. Delete them in the
% trunc_answers.
K16_infty_1 = answers(1:(m-7),:);
sched_e_home1 = team_name_e(K16_infty_1); % eastern conference home game schedule infty_1
sched_w_home1 = team_name_w(K16_infty_1); % western conference home game schedule infty_1

sched_e_away1 = [sched_e_home1(:,2), sched_e_home1(:,1)]; % eastern conference away game schedule infty_1
sched_w_away1 = [sched_w_home1(:,2), sched_w_home1(:,1)]; % western conference away game schedule infty_1
%%%%%%%% this chunk for separating schedules into individual files %%%%%%
mat = sched_e_home1;
[a, b] = size(mat);
base_path = pwd;
subfolder{1} = '\before_removal_eastern_schedules\';
path = [pwd subfolder{1}];
name = [conf(1,:) '_' h_or_a(1,:) '_day_'];
for i = 1:(a/7)
    temp = mat(((i-1)*7+1): i*7, :);
    save([path name num2str(i) '.mat'],'temp')
end
%%%%%%%% stop here %%%%%%


%%%%%%%% this chunk for separating schedules into individual files %%%%%%
mat = sched_w_home1;
[a, b] = size(mat);
base_path = pwd;
subfolder{2} = '\before_removal_western_schedules\';
path = [pwd subfolder{2}];
name = [conf(2,:) '_' h_or_a(1,:) '_day_'];
for i = 1:(a/7)
    temp = mat(((i-1)*7+1): i*7, :);
    save([path name num2str(i) '.mat'],'temp')
end
%%%%%%%% stop here %%%%%%


%%%%%%%% this chunk for separating schedules into individual files %%%%%%
mat = sched_e_away1;
[a, b] = size(mat);
base_path = pwd;
subfolder{3} = '\before_removal_eastern_schedules\';
path = [pwd subfolder{3}];
name = [conf(1,:) '_' h_or_a(2,:) '_day_'];
for i = 1:(a/7)
    temp = mat(((i-1)*7+1): i*7, :);
    save([path name num2str(i) '.mat'],'temp')
end
%%%%%%%% stop here %%%%%%


%%%%%%%% this chunk for separating schedules into individual files %%%%%%
mat = sched_w_away1;
[a, b] = size(mat);
base_path = pwd;
subfolder{4} = '\before_removal_western_schedules\';
path = [pwd subfolder{4}];
name = [conf(2,:) '_' h_or_a(2,:) '_day_'];
for i = 1:(a/7)
    temp = mat(((i-1)*7+1): i*7, :);
    save([path name num2str(i) '.mat'],'temp')
end
%%%%%%%% stop here %%%%%%

%% shifted index
K16_infty_2 = answers(8:112,:); % infinity portal paired with vertex 2
sched_e_home2 = team_name_e(K16_infty_2); % eastern conference home game schedule infty_2
sched_w_home1_copy = sched_w_home1; % western conference home game schedule infty_1

sched_e_away2 = [sched_e_home2(:,2), sched_e_home2(:,1)]; % eastern conference away game infty_2
sched_w_away1_copy = sched_w_away1; % western conference home game schedule infty_1 
% notice that the western conference has two copies of each K16


%%%%%%%% this chunk for separating schedules into individual files %%%%%%
mat = sched_e_home2;
[a, b] = size(mat);
base_path = pwd;
subfolder{1} = '\before_removal_eastern_schedules\';
path = [pwd subfolder{1}];
name = [conf(1,:) '_' h_or_a(1,:) '_sday_'];
for i = 1:(a/7)
    temp = mat(((i-1)*7+1): i*7, :);
    save([path name num2str(i) '.mat'],'temp')
end
%%%%%%%% stop here %%%%%%


%%%%%%%% this chunk for separating schedules into individual files %%%%%%
mat = sched_w_home1_copy;
[a, b] = size(mat);
base_path = pwd;
subfolder{2} = '\before_removal_western_schedules\';
path = [pwd subfolder{2}];
name = [conf(2,:) '_' h_or_a(1,:) '_sday_'];
for i = 1:(a/7)
    temp = mat(((i-1)*7+1): i*7, :);
    save([path name num2str(i) '.mat'],'temp')
end
%%%%%%%% stop here %%%%%%


%%%%%%%% this chunk for separating schedules into individual files %%%%%%
mat = sched_e_away2;
[a, b] = size(mat);
base_path = pwd;
subfolder{3} = '\before_removal_eastern_schedules\';
path = [pwd subfolder{3}];
name = [conf(1,:) '_' h_or_a(2,:) '_sday_'];
for i = 1:(a/7)
    temp = mat(((i-1)*7+1): i*7, :);
    save([path name num2str(i) '.mat'],'temp')
end
%%%%%%%% stop here %%%%%%


%%%%%%%% this chunk for separating schedules into individual files %%%%%%
mat = sched_w_away1_copy;
[a, b] = size(mat);
base_path = pwd;
subfolder{4} = '\before_removal_western_schedules\';
path = [pwd subfolder{4}];
name = [conf(2,:) '_' h_or_a(2,:) '_sday_'];
for i = 1:(a/7)
    temp = mat(((i-1)*7+1): i*7, :);
    save([path name num2str(i) '.mat'],'temp')
end
%%%%%%%% stop here %%%%%%

%% removal from intra-conf
% rm_x1 is for eastern conf game removal; rm_x2 is for western conf
[rm_a1, rm_a2] = A_home_remv; [rm_b1, rm_b2] = B_home_remv; [rm_c1, rm_c2] = C_home_remv; 
rm_e = [rm_a1(1:5,:); rm_b1(1:5,:); rm_c1(1:5,:)];
rm_w = [rm_a2(1:5,:); rm_b2(1:5,:); rm_c2(1:5,:)];
rm = [rm_e; rm_w];

% still tweaking.........
% conf = ['east';'west']; 
% h_or_a = ['home';'away'];
% 
% all_games = {K16_infty_2, [K16_infty_2(:,2), K16_infty_2(:,1)];
%              K16_infty_1,[K16_infty_1(:,2), K16_infty_1(:,1)]};
% 
% base_path = pwd;
% folder = '\after_removal_eastern_schedules\';
% for j = 1:2
%     mat = cell2mat(all_games(j));
%     [a, b] = size(mat);
%     for k = 1:2
%         for i = 1:(a/7)
%             temp = mat(((i-1)*7+1): i*7, :);
%             [rmd,ia] = setdiff(temp,rm,'rows','stable');
%             games = team_name_e(rmd);
%             save_to_mat(games, conf(k,:), h_or_a(k,:), folder)
%         end
%     end
% end
%% removal
% remove eastern conference home games
mat = K16_infty_2;
[a, b] = size(mat);
base_path = pwd;
subfolder{1} = '\schedules\';
path = [pwd subfolder{1}];
name = [conf(1,:) '_' h_or_a(1,:) '_day_'];
for i = 1:(a/7)
    temp = mat(((i-1)*7+1): i*7, :);
    [rmd,ia] = setdiff(temp,rm,'rows','stable');
    games = team_name_e(rmd);
    save([path name num2str(i) '.mat'],'games')
end

% remove eastern conference away games
mat = [K16_infty_2(:,2), K16_infty_2(:,1)];
[a, b] = size(mat);
base_path = pwd;
subfolder{1} = '\schedules\';
path = [pwd subfolder{1}];
name = [conf(1,:) '_' h_or_a(2,:) '_day_'];
for i = 1:(a/7)
    temp = mat(((i-1)*7+1): i*7, :);
    [rmd,ia] = setdiff(temp,rm,'rows','stable');
    games = team_name_e(rmd);
    save([path name num2str(i) '.mat'],'games')
end

% remove western conference home games
mat = K16_infty_1;
[a, b] = size(mat);
base_path = pwd;
subfolder{1} = '\schedules\';
path = [pwd subfolder{1}];
name = [conf(2,:) '_' h_or_a(1,:) '_day_'];
for i = 1:(a/7)
    temp = mat(((i-1)*7+1): i*7, :);
    [rmd,ia] = setdiff(temp,rm,'rows','stable');
    games = team_name_w(rmd);
    save([path name num2str(i) '.mat'],'games')
end

% remove western conference away games
mat = [K16_infty_1(:,2), K16_infty_1(:,1)];
[a, b] = size(mat);
base_path = pwd;
subfolder{1} = '\schedules\';
path = [pwd subfolder{1}];
name = [conf(2,:) '_' h_or_a(2,:) '_day_'];
for i = 1:(a/7)
    temp = mat(((i-1)*7+1): i*7, :);
    [rmd,ia] = setdiff(temp,rm,'rows','stable');
    games = team_name_w(rmd);
    save([path name num2str(i) '.mat'],'games')
end